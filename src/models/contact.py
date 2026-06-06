from pydantic import BaseModel


class Contact(BaseModel):
    name: str
    title: str
    linkedin_url: str
    company_domain: str