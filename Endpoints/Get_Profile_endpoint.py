import requests
class Profile:
    response = None
    request = None
    def get_profile(self, token):
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        self.response = requests.get(
        'https://stage-api.qomek.net/client/api/profile',
        headers = headers
    ).json()
        userId = self.response.get('userId')
        if userId:
            print(f"userId: {userId}")
        else:
            print("userId not found in the response")
    def checkResponse(self):
        assert 'userId' in self.response