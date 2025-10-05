import requests
import json
import pytest


@pytest.fixture(scope="session", autouse=True)
def all_tests_fixture():
    print("\nStart testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def each_test_fixture():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def new_object_id():
    body = json.dumps({
        "name": "Test object",
        "data": {
            "color": "Green",
            "size": "Medium",
        },
    })
    headers = {'Content-type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        data=body,
        headers=headers,
    )
    post_id = response.json()['id']
    yield post_id
    requests.delete(
        f'http://objapi.course.qa-practice.com/object/{post_id}'
    )


@pytest.mark.critical
@pytest.mark.parametrize(
    "name,color,size",
    [
        ("Test object 1", "Green", "Medium"),
        ("Test object 2", "Red", "Small"),
        ("Test object 3", "Blue", "Large"),
    ]
)
def test_create_object_successfully(name, color, size):
    body = json.dumps({
        "name": name,
        "data": {"color": color, "size": size},
    })
    headers = {'Content-type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        data=body,
        headers=headers,
    )
    assert response.status_code == 200
    print('Create obj')


@pytest.mark.medium
def test_update_object_with_put_successfully(new_object_id):
    body = json.dumps({
        "name": "Test object",
        "data": {
            "color": "Green",
            "size": "Large",
        },
    })
    headers = {'Content-type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        data=body,
        headers=headers,
    )
    assert response.status_code == 200
    print('Change data PUT')


def test_partial_update_object_with_patch_successfully(new_object_id):
    body = json.dumps({
        "data": {
            "color": "Red",
            "size": "Medium",
        },
    })
    headers = {'Content-type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        data=body,
        headers=headers,
    )
    assert response.status_code == 200
    print('Change data PATCH')


def test_delete_object_successfully(new_object_id):
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}'
    )
    assert response.status_code == 200
    print('Delete obj')
