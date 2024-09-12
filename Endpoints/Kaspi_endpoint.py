import requests

class Kaspi:
    response = None
    def post_payment(self):
        self.response = requests.post(
        'https://kaspi.qomek.net:8030/payment/'
    )
        results = self.response.content
        print(results)
        return results

    def post_payment_complete(self):
        self.response = requests.post(
        'https://kaspi.qomek.net:8030/payment/complete'
    )
        results = self.response.content
        print(results)
        return results