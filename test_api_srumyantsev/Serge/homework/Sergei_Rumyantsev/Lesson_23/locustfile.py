from locust import task, HttpUser
import random


class ObjApiUser(HttpUser):
    response = None

    def on_start(self):
        payload = {
            "name": "Test object",
            "data": {"color": "Green", "size": "Large"}
        }
        response = self.client.post(
            "/object", json=payload, name="POST /object"
        )
        self.post_id = response.json()["id"]

    @task(1)
    def get_all_obj(self):
        self.client.get(
            '/object'
        )

    @task(3)
    def get_obj_by_random_id(self):
        self.client.get(
            f'/object/{random.choice([3382, 3385, 3388, 3391])}'
        )

    @task
    def get_obj_by_post_id(self):
        self.client.get(
            f'/object/{self.post_id}',
        )
