import threading

from fastapi import HTTPException

from utils.email import email_utility
def email_send_service(email_to, email_subject, email_body):

    try:
        # Heavy Process Managing By Thread / Long Process
        threading.Thread(
            target=email_utility,
            args=(email_to, email_subject, email_body),
            daemon=True
        ).start()

        #email_utility(email_to, email_subject, email_body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
