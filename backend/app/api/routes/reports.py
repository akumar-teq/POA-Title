from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/report")
def get_report():

    return FileResponse(
        "storage/reports/report.pdf"
    )
