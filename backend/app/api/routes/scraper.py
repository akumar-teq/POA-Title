from fastapi import APIRouter

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