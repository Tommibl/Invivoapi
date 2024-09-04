import pytest
from Asserts import Asserts
from Endpoints.Cities_endpoint import Cities

@pytest.mark.test
@pytest.mark.run(order=1)
def test_Cities(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    cities = Cities()
    response = cities.get_cities(token=token)
    asserts = Asserts()
    asserts.check_response_status_200(response)