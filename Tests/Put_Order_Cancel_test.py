import pytest
from Asserts import Asserts
from Endpoints.Put_Order_Cancel_endpoint import Order_Cancel
from Models.Order_Cancel_Model import order_Cancel_Data


@pytest.mark.test
@pytest.mark.run(order=14)
def test_Put_Order_Cancel(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    order = Order_Cancel()
    response = order.put_Order_Cancel(order_Cancel_Data, token)
    asserts = Asserts()
    asserts.CheckResponse_notEmpty(response)
