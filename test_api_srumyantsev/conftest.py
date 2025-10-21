import pytest
from test_api_srumyantsev.endpoints.create_post import CreatePost
from test_api_srumyantsev.endpoints.update_post import UpdatePost
from test_api_srumyantsev.endpoints.partial_update_post import PartUpdatePost
from test_api_srumyantsev.endpoints.delete_post import DeletePost


@pytest.fixture
def create_post_endpoint(base_url):
    return CreatePost(base_url)


@pytest.fixture
def update_data_put(base_url):
    return UpdatePost(base_url)


@pytest.fixture
def update_data_patch(base_url):
    return PartUpdatePost(base_url)


@pytest.fixture
def delete_data(base_url):
    return DeletePost(base_url)


@pytest.fixture
def base_url():
    return 'http://objapi.course.qa-practice.com/object'


@pytest.fixture
def post_id(base_url):
    endpoint = CreatePost(base_url)
    body = {
        "name": "Test object",
        "data": {
            "color": "Green",
            "size": "Large",
        }
    }

    response = endpoint.create_new_post(body, headers=None)

    response_json = response.json()
    post_id = response_json["id"]

    return post_id
