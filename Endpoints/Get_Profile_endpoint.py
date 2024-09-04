import requests
class Profile:
    response = None
    def get_profile(self, token):
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        self.response = requests.get(
        'https://stage-api.qomek.net/client/api/profile',
        headers = headers
    ).json()
        print(self.response)
        return self.response