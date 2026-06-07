import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from services.ocean_service import OceanService


def test_ocean():

    service = OceanService()

    result = service.get_similar_companies(
        "google.com"
    )

    assert len(result) > 0