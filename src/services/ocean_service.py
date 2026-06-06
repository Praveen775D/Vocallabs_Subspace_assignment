from utils.logger import app_logger


class OceanService:

    def get_similar_companies(
        self,
        domain
    ):

        app_logger.info(
            f"Searching similar companies for {domain}"
        )

        return [

            "hubspot.com",

            "intercom.com",

            "zendesk.com",

            "freshworks.com",

            "zoho.com"
        ]