import requests
import json
import pytest
import allure


@allure.feature("Создание объекта")
@allure.story("Проверка создания объекта с параметрами")
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
    with allure.step("Формирование body запроса"):
        body = json.dumps({
            "name": name,
            "data": {
                "color": color,
                "size": size,
            },
        })
        headers = {'Content-type': 'application/json'}
    with allure.step("Отправка POST запроса и проверка результата"):
        response = requests.post(
            'http://objapi.course.qa-practice.com/object',
            data=body,
            headers=headers,
        )
        allure.attach(
            str(response.text), "Ответ сервера", allure.attachment_type.TEXT
        )
        assert response.status_code == 200


@allure.feature("Изменение объекта")
@allure.story("PUT изменение данных")
@pytest.mark.medium
def test_change_data_put(new_post_id):
    with allure.step("Формирование данных PUT запроса"):
        body = json.dumps({
            "name": "Test object",
            "data": {
                "color": "Green",
                "size": "Large",
            },
        })
        headers = {'Content-type': 'application/json'}
    with allure.step("Отправка PUT запроса"):
        response = requests.put(
            f'http://objapi.course.qa-practice.com/object/{new_post_id}',
            data=body,
            headers=headers,
        )
        allure.attach(
            str(response.text), "Ответ сервера", allure.attachment_type.TEXT
        )
        assert response.status_code == 200


@allure.feature("Изменение объекта")
@allure.story("PATCH частичное изменение данных")
def test_change_data_patch(new_post_id):
    with allure.step("Формирование данных PATCH запроса"):
        body = json.dumps({
            "data": {
                "color": "Red",
                "size": "Medium",
            },
        })
        headers = {'Content-type': 'application/json'}
    with allure.step("Отправка PATCH запроса"):
        response = requests.patch(
            f'http://objapi.course.qa-practice.com/object/{new_post_id}',
            data=body,
            headers=headers,
        )
        allure.attach(
            str(response.text), "Ответ сервера", allure.attachment_type.TEXT
        )
        assert response.status_code == 200


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
        f'http://objapi.course.qa-practice.com/object/{post_id}'
    )
