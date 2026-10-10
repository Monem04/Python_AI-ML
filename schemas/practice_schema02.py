from pydantic import BaseModel

class EmailRequest(BaseModel):
    email_to: str
    email_subject: str
    email_body: str