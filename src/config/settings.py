import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    OCEAN_API_KEY = os.getenv("OCEAN_API_KEY")

    PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")

    EAZYREACH_API_KEY = os.getenv("EAZYREACH_API_KEY")

    BREVO_API_KEY = os.getenv("BREVO_API_KEY")

    BREVO_SENDER_EMAIL = os.getenv("BREVO_SENDER_EMAIL")

    BREVO_SENDER_NAME = os.getenv("BREVO_SENDER_NAME")


settings = Settings()

print(settings.BREVO_SENDER_NAME)