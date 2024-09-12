import pytest
from Asserts import Asserts
from Endpoints.Get_Order_endpoint import Order

@pytest.mark.test
@pytest.mark.run(order=13)
def test_Get_Order(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    order = Order()
    response = order.get_Order(token)
    asserts = Asserts()
    asserts.CheckResponse_notEmpty(response)
