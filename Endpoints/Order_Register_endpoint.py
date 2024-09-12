import requests

class Register:
    response = None
    resp = None
    def post_register(self, request, token):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        self.response = requests.post(
        'https://stage-api.qomek.net/order/api/order/register',
        headers = headers,
        json=request
    ).json()
        print(self.response)
        return self.response