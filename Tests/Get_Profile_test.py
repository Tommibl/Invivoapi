import pytest

from Endpoints.Get_Profile_endpoint import Profile
@pytest.mark.test
@pytest.mark.run(order=1)
def test_Profile(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    if not token:
        pytest.fail("Access token not found in the response")
    profile = Profile()
    profile.get_profile(token=token)
    profile.checkResponse()

