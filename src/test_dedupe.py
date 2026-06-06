from models.email import EmailContact
from utils.dedupe import dedupe_emails

emails = [

    EmailContact(
        email="john@test.com",
        name="John",
        company_domain="test.com"
    ),

    EmailContact(
        email="john@test.com",
        name="John",
        company_domain="test.com"
    ),

    EmailContact(
        email="jane@test.com",
        name="Jane",
        company_domain="test.com"
    )
]

result = dedupe_emails(emails)

print(len(result))