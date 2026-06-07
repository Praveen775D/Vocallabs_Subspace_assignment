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

from services.prospeo_service import ProspeoService


def test_prospeo():

    service = ProspeoService()

    result = service.find_decision_makers(
        "google.com"
    )

    assert len(result) > 0