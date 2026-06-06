from models.contact import Contact


class ProspeoService:

    def find_decision_makers(
        self,
        domain
    ):

        return [

            Contact(
                name="John Doe",
                title="CEO",
                linkedin_url="https://linkedin.com/in/john",
                company_domain=domain
            ),

            Contact(
                name="Jane Smith",
                title="VP Sales",
                linkedin_url="https://linkedin.com/in/jane",
                company_domain=domain
            )

        ]