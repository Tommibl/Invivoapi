import requests
class Labs:
    response = None
    def post_labs(self, token):
        headers = {
            'Authorization': f'Bearer {token}',
            'language': 'ru',
            'country': 'KZ',
            'regionCode': 'KZ_R_4'
        }
        self.response = requests.post(
        'https://stage-api.qomek.net/laboratory/api/Labs/find?countryCode=KZ',
        headers = headers
    )
        results = self.response.content
        print(results)
        return results