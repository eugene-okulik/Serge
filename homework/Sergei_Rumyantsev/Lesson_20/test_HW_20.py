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
def new_post_id():
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
        f'http://objapi.course.qa-practice.com/object/{new_post_id}'
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
def test_create_post(name, color, size):
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
    assert response.status_code == 200
    print('Create obj')


@pytest.mark.medium
def test_change_data_put(new_post_id):
    body = json.dumps({
        "name": "Test object",
        "data": {
            "color": "Green",
            "size": "Large",
        },
    })
    headers = {'Content-type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}',
        data=body,
        headers=headers,
    )
    assert response.status_code == 200
    print('Change data PUT')


def test_change_data_patch(new_post_id):
    body = json.dumps({
        "data": {
            "color": "Red",
            "size": "Medium",
        },
    })
    headers = {'Content-type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}',
        data=body,
        headers=headers,
    )
    assert response.status_code == 200
    print('Change data PATCH')
