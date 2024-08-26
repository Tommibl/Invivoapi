import requests
from Utils import LoggingMixin
from Models.Get_Countries_Model import ResponseDataCountries
class Countries(LoggingMixin):
    def __init__(self):
        self.expected_response_data = [
            ResponseDataCountries(id="63297eb2a229a87b4b361f59", name="Казахстан", code="KZ",
                                  icon="657aa42cdb1e1b5c70c10633"),
            ResponseDataCountries(id="648b055cdb030c70f2d1c4a1", name="Кыргызстан", code="KG",
                                  icon="64b78fe83c746dd5243e3651"),
            ResponseDataCountries(id="6659680f623408b92551ba79", name="Узбекистан", code="UZ",
                                  icon="6659680f2d12569002a1233c")
        ]
    def get_countries(self, token):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.get(
            'https://stage-api.qomek.net/geo/api/Countries',
            headers=headers
        ).json()
        self.response = [
            ResponseDataCountries(**item) for item in response
        ]
    def check_response(self):
        print("Response Data:", self.response)
        print("Expected Data:", self.expected_response_data)
        response_data_set = {tuple(vars(item).items()) for item in self.response}
        expected_data_set = {tuple(vars(item).items()) for item in self.expected_response_data}
        assert response_data_set == expected_data_set, "Response data does not match expected data"

