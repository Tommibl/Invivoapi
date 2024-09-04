import pytest

from Asserts import Asserts
from Endpoints.Get_Profile_endpoint import Profile
@pytest.mark.test
@pytest.mark.run(order=1)
def test_Profile(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    profile = Profile()
    response = profile.get_profile(token=token)
    field = 'userId'
    asserts = Asserts()
    asserts.checkResponse_availability(field, response)