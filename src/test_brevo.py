from services.brevo_service import BrevoService

service = BrevoService()

service.send_email(
    "john@test.com",
    "John",
    "Test Subject",
    "Hello"
)