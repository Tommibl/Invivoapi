import pytest

from Asserts import Asserts
from Endpoints.Price_endpoint import Price
@pytest.mark.test
@pytest.mark.run(order=1)
def test_Price(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    price = Price()
    response = price.get_price(token=token)
    asserts = Asserts()
    asserts.CheckResponse_notEmpty(response)
