# from utils.email import email_utility
# from core.celery_app import celery_app
#
# @celery_app.task(bind=True)
# def email_send_service(self, email_to, email_subject, email_body):
#     try:
#         email_utility(email_to, email_subject, email_body)
#     except Exception as e:
#         raise self.retry(exc=e, max_retries=10)

from core.celery_app import celery_app  # আপনার celery_app ফাইলের পাথ অনুযায়ী ইমপোর্ট করুন
from utils.email import email_utility

@celery_app.task(name="services.practice_service04.email_send_service")
def email_send_service(email_to: str, email_subject: str, email_body: str):
    email_utility(email_to, email_subject, email_body)
    return f"Email sent to {email_to}"