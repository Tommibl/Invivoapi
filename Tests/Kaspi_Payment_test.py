import pytest
from Asserts import Asserts
from Endpoints.Kaspi_endpoint import Kaspi
@pytest.mark.test
@pytest.mark.run(order=11)
def test_Kaspi_Payment():
    kaspi = Kaspi()
    response = kaspi.post_payment()
    asserts = Asserts()
    asserts.CheckResponse_notEmpty(response)
@pytest.mark.test
@pytest.mark.run(order=12)
def test_Kaspi_Payment_Complete():
    kaspi = Kaspi()
    response = kaspi.post_payment_complete()
    asserts = Asserts()
    asserts.CheckResponse_notEmpty(response)
