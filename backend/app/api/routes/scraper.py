from fastapi import APIRouter
from pydantic import BaseModel

from app.services.scraper_service import (
    search_bexar
)

router = APIRouter()


@router.get("/search/{query}")
def search(query: str):

    results = search_bexar(query)

    return {
        "query": query,
        "results": results
    }

class DynamicSearchRequest(BaseModel):
    county: str
    owner_name: str
    property_address: str

def parse_name(full_name: str):
    # e.g., "Jeromy Deon White & Rachael Renee Liggins" -> "Jeromy Deon White"
    primary_name = full_name.split('&')[0].strip()
    parts = primary_name.split()
    if len(parts) >= 2:
        first_name = " ".join(parts[:-1])
        last_name = parts[-1]
    else:
        first_name = primary_name
        last_name = ""
    return first_name, last_name

@router.post("/search/dynamic")
def dynamic_search(request: DynamicSearchRequest):
    county = request.county.strip().lower()

    if "bexar" not in county:
        return {"error": f"Scraper for county '{county}' not currently supported."}

    first_name, last_name = parse_name(request.owner_name)
    street = request.property_address.split(',')[0].strip() if request.property_address else ""

    # Build search terms for the scraper
    # For name: typically last name or full first/last works. Let's pass the extracted name.
    # The scraping string for Name will be "FirstName LastName" and for Address it will be "Street"
    name_query = f"{first_name} {last_name}".strip()

    results = search_bexar(name_query, address_text=street)

    return {
        "county": county,
        "parsed": {
            "first_name": first_name,
            "last_name": last_name,
            "street": street
        },
        "query": {
            "name": name_query,
            "address": street
        },
        "results": results
    }