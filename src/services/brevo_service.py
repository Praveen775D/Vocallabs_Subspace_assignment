class BrevoService:

    def send_email(
        self,
        recipient_email,
        recipient_name,
        subject,
        content
    ):

        print(
            f"Sending email to {recipient_email}"
        )

        return True