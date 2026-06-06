from models.email import EmailContact

email = EmailContact(
    email="john@google.com",
    name="John Doe",
    company_domain="google.com"
)

print(email)