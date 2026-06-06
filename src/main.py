from services.ocean_service import get_similar_companies
from services.prospeo_service import get_contacts
from services.eazyreach_service import get_emails
from services.brevo_service import send_email

domain = input("Enter company domain: ")

companies = get_similar_companies(domain)

summary = []

for company in companies:
    contacts = get_contacts(company)
    emails = get_emails(contacts)

    for email in emails:
        summary.append(email)

print("Summary before sending:")
for s in summary:
    print(s)

confirm = input("Send emails? (y/n): ")

if confirm.lower() == "y":
    for email in summary:
        send_email(email)

print("Done")
