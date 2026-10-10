from fastapi import FastAPI, APIRouter, HTTPException

from schemas.practice_schema01 import EmailRequest
from services.practice_service01 import email_send_service

router = APIRouter()

# Manually ---------

@router.post("/practice01")
async def practice01(data: EmailRequest):
    try:
        email_send_service(data.email_to, data.email_subject, data.email_body)
        return {"message": "practice email send success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
