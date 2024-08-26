import pytest
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
        response = self.response
        print(self.response)
        if response.status_code == 401:
            pytest.fail("Unauthorized: Invalid or expired token")
        if not response.content:
            pytest.fail("Empty response received")