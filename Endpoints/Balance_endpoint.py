import requests

class Balance:
    response = None
    def get_balance(self, token):
        headers = {
            'Authorization': f'Bearer {token}',
            'language': 'ru',
            'country': 'KZ',
            'api-version':'2.0'
        }
        self.response = requests.get(
        'https://stage-api.qomek.net/billing/api/balance/bonuses?countryCode=KZ',
        headers = headers
    )
        results = self.response.content
        print(results)
        return results