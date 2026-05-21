import sys
import os
import ssl
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

# Ensure backend directory is in python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine
from app.models.county_model import County

TEXAS_COUNTIES = [
    "Anderson", "Andrews", "Angelina", "Aransas", "Archer", "Armstrong", "Atascosa", "Austin", "Bailey", "Bandera",
    "Bastrop", "Baylor", "Bee", "Bell", "Bexar", "Blanco", "Borden", "Bosque", "Bowie", "Brazoria",
    "Brazos", "Brewster", "Briscoe", "Brooks", "Brown", "Burleson", "Burnet", "Caldwell", "Calhoun", "Callahan",
    "Cameron", "Camp", "Carson", "Cass", "Castro", "Chambers", "Cherokee", "Childress", "Clay", "Cochran",
    "Coke", "Coleman", "Collin", "Collingsworth", "Colorado", "Comal", "Comanche", "Concho", "Cooke", "Coryell",
    "Cottle", "Crane", "Crockett", "Crosby", "Culberson", "Dallam", "Dallas", "Dawson", "Deaf Smith", "Delta",
    "Denton", "DeWitt", "Dickens", "Dimmit", "Donley", "Duval", "Eastland", "Ector", "Edwards", "Ellis",
    "El Paso", "Erath", "Falls", "Fannin", "Fayette", "Fisher", "Floyd", "Foard", "Fort Bend", "Franklin",
    "Freestone", "Frio", "Gaines", "Galveston", "Garza", "Gillespie", "Glasscock", "Goliad", "Gonzales", "Gray",
    "Grayson", "Gregg", "Grimes", "Guadalupe", "Hale", "Hall", "Hamilton", "Hansford", "Hardeman", "Hardin",
    "Harris", "Harrison", "Hartley", "Haskell", "Hays", "Hemphill", "Henderson", "Hidalgo", "Hill", "Hockley",
    "Hood", "Hopkins", "Houston", "Howard", "Hudspeth", "Hunt", "Hutchinson", "Irion", "Jack", "Jackson",
    "Jasper", "Jeff Davis", "Jefferson", "Jim Hogg", "Jim Wells", "Johnson", "Jones", "Karnes", "Kaufman", "Kendall",
    "Kenedy", "Kent", "Kerr", "Kimble", "King", "Kinney", "Kleberg", "Knox", "Lamar", "Lamb",
    "Lampasas", "La Salle", "Lavaca", "Lee", "Leon", "Liberty", "Limestone", "Lipscomb", "Live Oak", "Llano",
    "Loving", "Lubbock", "Lynn", "McCulloch", "McLennan", "McMullen", "Madison", "Marion", "Martin", "Mason",
    "Matagorda", "Maverick", "Medina", "Menard", "Midland", "Milam", "Mills", "Mitchell", "Montague", "Montgomery",
    "Moore", "Morris", "Motley", "Nacogdoches", "Navarro", "Newton", "Nolan", "Nueces", "Ochiltree", "Oldham",
    "Orange", "Palo Pinto", "Panola", "Parker", "Parmer", "Pecos", "Polk", "Potter", "Presidio", "Rains",
    "Randall", "Reagan", "Real", "Red River", "Reeves", "Refugio", "Roberts", "Robertson", "Rockwall", "Runnels",
    "Rusk", "Sabine", "San Augustine", "San Jacinto", "San Patricio", "San Saba", "Schleicher", "Scurry", "Shackelford", "Shelby",
    "Sherman", "Smith", "Somervell", "Starr", "Stephens", "Sterling", "Stonewall", "Sutton", "Swisher", "Tarrant",
    "Taylor", "Terrell", "Terry", "Throckmorton", "Titus", "Tom Green", "Travis", "Trinity", "Tyler", "Upshur",
    "Upton", "Uvalde", "Val Verde", "Van Zandt", "Victoria", "Walker", "Waller", "Ward", "Washington", "Webb",
    "Wharton", "Wheeler", "Wichita", "Wilbarger", "Willacy", "Williamson", "Wilson", "Winkler", "Wise", "Wood",
    "Yoakum", "Young", "Zapata", "Zavala"
]

def check_county_url(county_name):
    # Format url, e.g. "El Paso" -> "elpaso", "DeWitt" -> "dewitt"
    subdomain = county_name.lower().replace(" ", "")
    
    url_templates = [
        "https://{sub}.tx.publicsearch.us/",
        "https://{sub}countytx.govos.com/",
        "https://{sub}tx.countygovernmentrecords.com/",
        "https://{sub}.texaslandrecords.com/"
    ]
    
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    for template in url_templates:
        url = template.format(sub=subdomain)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            response = urllib.request.urlopen(req, context=context, timeout=4)
            if response.status == 200:
                return county_name, url
        except Exception:
            continue
            
    return county_name, None

def seed_counties():
    db: Session = SessionLocal()
    
    print(f"Pinging multiple domains for {len(TEXAS_COUNTIES)} counties. Please wait...")
    
    results = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_county_url, county): county for county in TEXAS_COUNTIES}
        
        for future in as_completed(futures):
            county_name = futures[future]
            try:
                name, url = future.result()
                results.append((name, url))
            except Exception as e:
                results.append((county_name, None))
                
    success_count = 0
    total_added = 0
    
    for name, url in results:
        # Check if exists
        existing = db.query(County).filter(County.name == name).first()
        
        if existing:
            # Update website if found now but wasn't before
            if url and not existing.website:
                existing.website = url
                success_count += 1
                print(f"Updated {name} -> {url}")
        else:
            # Insert logic: store ALL counties!
            new_county = County(name=name, website=url)
            db.add(new_county)
            total_added += 1
            if url:
                success_count += 1
                print(f"Added {name} -> {url}")
            else:
                print(f"Added {name} (No Website working)")
                
    db.commit()
    db.close()
    
    print(f"\nDone! Added {total_added} new counties. Total working endpoints found: {success_count}.")

if __name__ == "__main__":
    seed_counties()
