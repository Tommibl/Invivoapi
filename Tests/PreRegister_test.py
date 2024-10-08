import pytest
from Asserts import Asserts
from Endpoints.PreRegister_endpoint import PreRegister
from Models.PreRegister_Model import RequestData
@pytest.mark.test
@pytest.mark.run(order=8)
def test_Labs(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    request = RequestData().request_json
    preregister = PreRegister()
    response = preregister.post_preregister(request=request,token=token)
    asserts = Asserts()
    asserts.checkResponse_availability('value', response=response)
