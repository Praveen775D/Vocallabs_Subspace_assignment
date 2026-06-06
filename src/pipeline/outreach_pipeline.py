from services.ocean_service import OceanService
from services.prospeo_service import ProspeoService
from services.eazyreach_service import EazyreachService
from services.brevo_service import BrevoService

from utils.dedupe import dedupe_emails
from utils.email_templates import generate_email


class OutreachPipeline:

    def __init__(self):

        self.ocean = OceanService()

        self.prospeo = ProspeoService()

        self.eazyreach = EazyreachService()

        self.brevo = BrevoService()

    def run(self, domain):

        print(f"\nSeed Domain: {domain}")

        companies = self.ocean.get_similar_companies(domain)

        emails = []

        for company in companies:

            contacts = self.prospeo.find_decision_makers(
                company
            )

            for contact in contacts:

                email = self.eazyreach.resolve_email(
                    contact
                )

                emails.append(email)

        emails = dedupe_emails(emails)

        print("\nSUMMARY")

        print(
            f"Companies Found: {len(companies)}"
        )

        print(
            f"Emails Found: {len(emails)}"
        )

        choice = input(
            "\nSend Emails? (y/n): "
        )

        if choice.lower() != "y":

            print("Cancelled")

            return

        for email in emails:

            body = generate_email(
                email.name,
                email.company_domain
            )

            self.brevo.send_email(
                email.email,
                email.name,
                "Automated Outreach",
                body
            )

        print("\nPipeline Complete")