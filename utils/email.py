import smtplib
from email.mime.text import MIMEText
from fastapi import HTTPException
from core.config import SMTP_FROM, SMTP_PASSWORD, SMTP_HOST, SMTP_PORT


def email_utility(email_to, email_subject, email_body):
    msg = MIMEText(email_body)
    msg['Subject'] = email_subject
    msg['From'] = SMTP_FROM
    msg['To'] = email_to

    # connection ------------

    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        server.login(SMTP_FROM, SMTP_PASSWORD)
        server.sendmail(SMTP_FROM, email_to, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
        raise HTTPException(status_code=400, detail=str(e))

