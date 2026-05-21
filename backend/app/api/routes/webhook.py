from fastapi import APIRouter

router = APIRouter()

@router.get("/webhook")
def webhook():
    return {"message": "Webhook working"}
