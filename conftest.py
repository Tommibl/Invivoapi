import pytest
from Endpoints.Authorization_endpoint import Authorization, GetToken
from Models.Authorization_Models import RequestDataVerification, RequestDataToken


@pytest.fixture(scope='module')
def get_verification_token():
    verification_instance = Authorization()
    token_instance = GetToken()
    request_data = RequestDataVerification().requestBody

    # Получаем verification_token
    verification_instance.getVerification(request=request_data)
    verification_token = verification_instance.response.get('verificationToken')

    if not verification_token:
        pytest.fail("Verification token not found in the response")

    # Создаем объект RequestDataToken
    token_data = RequestDataToken(verification_token)

    # Получаем access_token
    token_instance.requestToken(request_data_token=token_data)

    if 'access_token' not in token_instance.response:
        pytest.fail("Access token not found in the response")

    return token_instance
