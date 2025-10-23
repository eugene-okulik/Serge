import requests
import allure
from test_api_srumyantsev.endpoints.endpoint import Endpoint


class Createobject(Endpoint):

    @allure.step('Create new object')
    def create_new_object(self, body, headers):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers,
        )
        self.json = self.response.json()
        return self.response
