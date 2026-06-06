from models.email import EmailContact


class EazyreachService:

    def resolve_email(
        self,
        contact
    ):

        first_name = (
            contact.name
            .split()[0]
            .lower()
        )

        return EmailContact(
            email=f"{first_name}@{contact.company_domain}",
            name=contact.name,
            company_domain=contact.company_domain
        )