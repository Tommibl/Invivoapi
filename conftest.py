import pytest
from endpoints.endpointAuthorization import Authorization
from models.AuthorizationModels import RequestDataVerification


@pytest.fixture(scope='module')
def get_verification_token():
    verification_instance = Authorization()
    request_data = RequestDataVerification().requestBody
    verification_instance.getVerification(request=request_data)

    verification_token = verification_instance.response.get('verificationToken')
    if not verification_token:
        pytest.fail("Verification token not found in the response")

    return verification_token