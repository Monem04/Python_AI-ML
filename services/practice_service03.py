from fastapi import HTTPException

from utils.email import email_utility
def email_send_service(email_to, email_subject, email_body):
    try:
        email_utility(email_to, email_subject, email_body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
