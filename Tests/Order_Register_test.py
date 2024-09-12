import pytest
from Asserts import Asserts
from Endpoints.Order_Register_endpoint import Register
from Models.Order_Register_Model import RegisterDataRequest, RegisterData


@pytest.mark.test
@pytest.mark.run(order=1)
def test_Balance(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    requestdata = RegisterDataRequest()
    register = Register()
    register.post_register(request=requestdata.register_data,token=token)
