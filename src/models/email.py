from pydantic import BaseModel


class EmailContact(BaseModel):
    email: str
    name: str
    company_domain: str