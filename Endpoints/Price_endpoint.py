import requests
class Price:
    response = None
    def get_price(self, token):
        headers = {
            'Authorization': f'Bearer {token}',
            'language': 'ru',
            'country': 'KZ',
            'regionCode': 'KZ_R_4'
        }
        self.response = requests.get(
        'https://stage-api.qomek.net/price/api/Price/'
        'findWithPaging?provider=Invivo&strFind=&regionCode=KZ_R_4&groupCode=&typeCode=research&page=1&pagesize=20',
        headers = headers
    )
        results = self.response.content
        if results:
            print(f"results: {results}")
        else:
            print("results not found in the response")