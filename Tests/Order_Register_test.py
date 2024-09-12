import pytest

from Asserts import Asserts
from Endpoints.Order_Register_endpoint import Register
from Models.Order_Register_Model import RegisterDataRequest, RegisterData


@pytest.mark.test
@pytest.mark.run(order=10)
def test_Order_Register(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    requestdata = RegisterDataRequest()
    register = Register()
    response = register.post_register(request=requestdata.register_data,token=token)
    asserts = Asserts()
    asserts.CheckResponse_notEmpty(response)
