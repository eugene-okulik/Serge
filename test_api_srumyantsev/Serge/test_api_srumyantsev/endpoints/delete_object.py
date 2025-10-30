import requests

from test_api_srumyantsev.endpoints.endpoint import Endpoint


class Deleteobject(Endpoint):

    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{object_id}',
            headers=headers,
        )
        self.json = self.response
        return self.response
