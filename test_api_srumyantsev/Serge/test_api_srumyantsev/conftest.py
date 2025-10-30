import pytest
from test_api_srumyantsev.endpoints.create_object import Createobject
from test_api_srumyantsev.endpoints.update_object import Updateobject
from test_api_srumyantsev.endpoints.partial_update_object import PartUpdateobject
from test_api_srumyantsev.endpoints.delete_object import Deleteobject


@pytest.fixture
def create_object_endpoint(base_url):
    return Createobject(base_url)


@pytest.fixture
def update_data_put(base_url):
    return Updateobject(base_url)


@pytest.fixture
def update_data_patch(base_url):
    return PartUpdateobject(base_url)


@pytest.fixture
def delete_data(base_url):
    return Deleteobject(base_url)


@pytest.fixture
def base_url():
    return 'http://objapi.course.qa-practice.com/object'


@pytest.fixture
def object_id(create_object_endpoint, delete_data, base_url):
    body = {
        "name": "Test object",
        "data": {
            "color": "Green",
            "size": "Large",
        }
    }

    response = create_object_endpoint.create_new_object(body=body, headers=None)

    response_json = response.json()
    object_id = response_json["id"]

    yield object_id

    delete_data.delete_object(object_id, headers=None)
