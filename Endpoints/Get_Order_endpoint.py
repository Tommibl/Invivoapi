import requests
class Order:
    response = None
    def get_Order(self, token):
        headers = {
            'Authorization': f'Bearer {token}',
        }
        self.response = requests.get(
        'https://stage-api.qomek.net/order/api/order/byId/id=66d804609330d8fce81f16c7',
        headers = headers
    ).json
        print(self.response)
        return self.response