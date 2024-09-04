import pytest
from Asserts import Asserts
from Endpoints.Get_Countries_endpoint import Countries
from Models.Get_Countries_Model import ResponseDataCountries

expected_response_data = [
            ResponseDataCountries(id="63297eb2a229a87b4b361f59", name="Казахстан", code="KZ",
                                  icon="657aa42cdb1e1b5c70c10633"),
            ResponseDataCountries(id="648b055cdb030c70f2d1c4a1", name="Кыргызстан", code="KG",
                                  icon="64b78fe83c746dd5243e3651"),
            ResponseDataCountries(id="6659680f623408b92551ba79", name="Узбекистан", code="UZ",
                                  icon="6659680f2d12569002a1233c")
        ]

@pytest.mark.test
@pytest.mark.run(order=1)
def test_Countries(get_verification_token):
    token_instance = get_verification_token
    token = token_instance.response.get('access_token')
    countries = Countries()
    response = countries.get_countries(token=token)
    asserts = Asserts()
    asserts.check_response_equal(response, expected_response_data)

