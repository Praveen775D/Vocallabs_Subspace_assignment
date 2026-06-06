from services.eazyreach_service import EazyreachService
from models.contact import Contact

contact = Contact(
    name="John Doe",
    title="CEO",
    linkedin_url="https://linkedin.com/in/john",
    company_domain="google.com"
)

service = EazyreachService()

print(
    service.resolve_email(contact)
)