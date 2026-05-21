from app.services.scraper_service import search_bexar

if __name__ == "__main__":
    print("Testing Bexar Scraper with 'SMITH JOHN'...")
    res = search_bexar("SMITH JOHN")
    print("\nFinal Results:")
    for r in res.get("results", []):
        print(f" - {r}")
