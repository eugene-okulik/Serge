import requests

from test_api_srumyantsev.endpoints.endpoint import Endpoint


class Updateobject(Endpoint):

    def make_changes_in_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers,
        )
        self.json = self.response.json()
        return self.response
