from services.ocean_service import OceanService

service = OceanService()

companies = service.get_similar_companies(
    "google.com"
)

print(companies)