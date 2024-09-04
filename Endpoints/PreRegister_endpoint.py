import requests

class PreRegister:
    response = None
    def post_preregister(self, request, token):
        headers = {
            'Authorization': f'Bearer {token}',
            'language': 'ru',
            'country': 'KZ',
            'regionCode': 'KZ_R_4'
        }
        self.response = requests.post(
        'https://stage-api.qomek.net/order/api/Order/preRegister',
        headers = headers,
        json = request
    )
        results = self.response.content
        print(results)
        return results