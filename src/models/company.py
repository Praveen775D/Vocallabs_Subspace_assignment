from pydantic import BaseModel


class Company(BaseModel):
    domain: str