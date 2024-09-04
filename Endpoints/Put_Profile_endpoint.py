
import requests
class Put_Profile:
    response = None
    request = None
    def put_profile(self, request, token):
        headers = {
            'Authorization': f'Bearer {token}'
        }
        self.response = requests.put(
        'https://stage-api.qomek.net/client/api/profile',
        headers = headers,
        json = request
        )
        print(self.response)
        return self.response