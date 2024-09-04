import requests

class Cities:
    response = None
    def get_cities(self, token):
        headers = {
            'Authorization': f'Bearer {token}',
            'language': 'ru',
            'country': 'KZ',
            'regionCode': 'KZ_R_4'
        }
        self.response = requests.get(
        'https://stage-api.qomek.net/geo/api/Cities/ByCountry',
        headers = headers
    )
        return self.response
    #def check_response_status(self):
        #assert self.response.status_code == 200, f"Expected status 200, but got {self.response['status']}"