import requests
import json


def create():
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
    ).json()
    return response


post_data = create()
post_id = 0
for key, value in post_data.items():
    if key == 'id':
        post_id = value


def change_data_put():
    body = json.dumps({
        "name": "Test object",
        "data": {
            "color": "Green",
            "size": "Large",
        },
    })
    headers = {'Content-type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        data=body,
        headers=headers,
    ).json()
    return response


put_data = change_data_put()
put_size = ''
for key, value in put_data.items():
    if key == 'data':
        for data_key, data_value in value.items():
            if data_key == 'size':
                put_size = data_value


def change_data_patch():
    body = json.dumps({
        "data": {
            "color": "Red",
            "size": put_size,
        },
    })
    headers = {'Content-type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        data=body,
        headers=headers,
    ).json()
    print(response)


change_data_patch()


def delete_data():
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


delete_data()
