import requests
from urllib3 import request


class Order_Cancel:
    response = None
    def put_Order_Cancel(self, request, token):
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        self.response = requests.put(
        'https://stage-api.qomek.net/order/api/order/cancel?deviceId=F379512C-AC2C-4503-A651-7617F3285E46&id=66d806d39330d8fce81f16d4&userId=c0aa7fe7-8bb7-4208-8a04-87a0a299dabc',
        headers = headers,
        json = request
    ).json()
        print(self.response)
        return self.response