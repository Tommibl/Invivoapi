import requests
from Utils import LoggingMixin
from Models.Get_Countries_Model import ResponseDataCountries
class Countries(LoggingMixin):
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
        return self.response

