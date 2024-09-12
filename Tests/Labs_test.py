import pytest

from Asserts import Asserts
from Endpoints.Labs_endpoint import Labs
@pytest.mark.test
@pytest.mark.run(order=6)
def test_Labs(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    labs = Labs()
    response = labs.post_labs(token=token)
    asserts = Asserts()
    asserts.CheckResponse_notEmpty(response)
