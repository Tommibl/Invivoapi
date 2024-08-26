import requests


class Authorization:
    def __init__(self):
        self.response = ''

    def getVerification(self, request):
        self.response = requests.post(
        'https://identity.qomek.net/api/verification',
            json=request
        ).json()

        verification_token = self.response.get('verificationToken')

        if verification_token:
            print(f"Verification Token: {verification_token}")
        else:
            print("Verification Token not found in the response")

    def checkResponse(self):
        assert 'verificationToken' in self.response


class GetToken:

    def __init__(self):
       self.response = ''

    def requestToken(self, request_data_token):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # Получаем закодированное тело запроса
        encoded_body = request_data_token.get_encoded_body()
        self.response = requests.post(
            'https://identity.qomek.net/connect/token',
            data=encoded_body,
            headers=headers
        ).json()
        print(self.response)

    def checkResponse(self):
        assert 'access_token' in self.response, "Access token not found in the response"


if __name__ == '__main__':
    get_token = GetToken()
    get_token.checkResponse()