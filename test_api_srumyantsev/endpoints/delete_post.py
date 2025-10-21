import requests

from test_api_srumyantsev.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):

    def delete_post(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{post_id}',
            headers=headers,
        )
        self.json = self.response
        return self.response
