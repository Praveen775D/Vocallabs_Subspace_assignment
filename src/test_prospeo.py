from services.prospeo_service import ProspeoService

service = ProspeoService()

contacts = service.find_decision_makers(
    "google.com"
)

for contact in contacts:

    print(contact)