from fastapi import FastAPI, APIRouter, BackgroundTasks, HTTPException

from schemas.practice_schema03 import EmailRequest
from services.practice_service03 import email_send_service

router = APIRouter()

@router.post("/practice03")
async def practice03(data: EmailRequest,background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(
            email_send_service(data.email_to, data.email_subject, data.email_body)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
