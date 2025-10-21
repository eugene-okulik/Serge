import requests

from test_api_srumyantsev.endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):

    def make_changes_in_post(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            json=body,
            headers=headers,
        )
        self.json = self.response.json()
        return self.response
