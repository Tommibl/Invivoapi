import pytest

from Asserts import Asserts
from Endpoints.Put_Profile_endpoint import Put_Profile
from Models.Put_Profile_Model import Request_Data_Put_Profile
@pytest.mark.test
@pytest.mark.run(order=1)
def test_Put_Profile(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    request_data = Request_Data_Put_Profile()
    endpoint = Put_Profile()
    response = endpoint.put_profile(request=request_data.requestBody, token=token)
    asserts = Asserts()
    asserts.check_response_status_200(response)
