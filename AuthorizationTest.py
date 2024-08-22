
import pytest

from endpoints.endpointAuthorization import GetToken, Authorization
from models.AuthorizationModels import RequestDataVerification, RequestDataToken


@pytest.mark.test
@pytest.mark.run(order=1)
def test_Verification():
    data = RequestDataVerification()
    verification = Authorization()
    verification.getVerification(request=data.requestBody)
    verification.checkResponse()


@pytest.mark.test
@pytest.mark.run(order=2)
def test_Token():
    verification_instance = Authorization()
    verification_instance.getVerification(request=RequestDataVerification().requestBody)
    verificationToken = verification_instance.response.get('verificationToken')

    if not verificationToken:
        pytest.fail("Verification token not found in the response")

    data = RequestDataToken(verificationToken)

    getToken = GetToken()
    getToken.requestToken(request_data_token=data)

    # Проверяем ответ
    getToken.checkResponse()
