import pytest

from Endpoints.Get_Profile_endpoint import Profile
from Endpoints.Labs_endpoint import Labs


@pytest.mark.test
@pytest.mark.run(order=1)
def test_Labs(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    if not token:
        pytest.fail("Access token not found in the response")
    labs = Labs()
    labs.post_labs(token=token)

