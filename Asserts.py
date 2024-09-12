class Asserts:
    def check_response_status_200(self, response):
        assert response.status_code == 200, f"Expected status 200, but got {response['status']}"

    def check_response_equal(self, response, expected_response_data):
        print("Response Data:", response)
        print("Expected Data:", expected_response_data)
        response_data_set = {tuple(vars(item).items()) for item in response}
        expected_data_set = {tuple(vars(item).items()) for item in expected_response_data}
        assert response_data_set == expected_data_set, "Response data does not match expected data"

    def checkResponse_availability(self, field, response):
        if isinstance(response, bytes):
            resp = response.decode('utf-8')
        else:
            resp = response
        assert field in resp, "Field absent"

    def CheckResponse_notEmpty(self, response):
        assert response, "Response is empty!"