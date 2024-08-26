import pytest
from Endpoints.Get_Countries_endpoint import Countries
@pytest.mark.test
@pytest.mark.run(order=1)
def test_Countries(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    if not token:
        pytest.fail("Access token not found in the response")
    countries = Countries()
    countries.get_countries(token=token)
    countries.check_response()

