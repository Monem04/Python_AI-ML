from fastapi import FastAPI, APIRouter, HTTPException

from schemas.practice_schema02 import EmailRequest
from services.practice_service02 import email_send_service

router = APIRouter()

@router.post("/practice02")
async def practice01(data: EmailRequest):
    #schema
    #service
    #
    try:
        email_send_service(data.email_to, data.email_subject, data.email_body)
        return {"message": "practice email sent success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
