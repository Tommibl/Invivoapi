import pytest
from Asserts import Asserts
from Endpoints.Balance_endpoint import Balance
@pytest.mark.test
@pytest.mark.run(order=1)
def test_Balance(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    field = 'balance'
    balance = Balance()
    response = balance.get_balance(token=token)
    asserts = Asserts()
    asserts.checkResponse_availability(field, response)
