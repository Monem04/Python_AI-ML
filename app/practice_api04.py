# from fastapi import FastAPI, APIRouter, HTTPException
#
# from schemas.practice_schema04 import EmailRequest
# from services.practice_service04 import email_send_service
#
# router = APIRouter()
#
# # Manually ---------
#
# @router.post("/practice04")
# async def practice04(data: EmailRequest):
#     try:
#         task=email_send_service.delay(data.email_to, data.email_subject, data.email_body)
#         return {"message": "practice email send success",
#                 "task_id": task.id
#                 }
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


from fastapi import APIRouter, HTTPException
from schemas.practice_schema04 import EmailRequest
from services.practice_service04 import email_send_service

router = APIRouter()

@router.post("/practice04")
async def practice04(data: EmailRequest):
    try:
        # .delay() কল করার মাধ্যমে টাস্কটি RabbitMQ-তে জমা হবে
        task = email_send_service.delay(
            data.email_to,
            data.email_subject,
            data.email_body
        )
        return {
            "message": "practice email task queued successfully",
            "task_id": task.id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))