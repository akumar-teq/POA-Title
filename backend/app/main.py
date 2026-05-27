from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from app.api.routes.webhook import router as webhook_router
from app.api.routes.reports import router as reports_router
from app.api.routes.upload import router as upload_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.process import router as process_router
from app.api.routes.scraper import router as scraper_router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(scraper_router)
app.include_router(reports_router)
app.include_router(webhook_router)
app.include_router(process_router)

@app.get("/")
def home():
    return {"message": "POA Title API Running"}
