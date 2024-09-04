import pytest
from Endpoints.Price_endpoint import Price


@pytest.mark.test
@pytest.mark.run(order=1)
def test_Price(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    if not token:
        pytest.fail("Access token not found in the response")
    price = Price()
    price.get_price(token=token)
