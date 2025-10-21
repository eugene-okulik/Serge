import requests
import allure
from test_api_srumyantsev.endpoints.endpoint import Endpoint


class CreatePost(Endpoint):

    def build_body(self, name, color, size):
        return {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }

    @allure.step('Create new post')
    def create_new_post(self, body, headers):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers,
        )
        self.json = self.response.json()
        return self.response
