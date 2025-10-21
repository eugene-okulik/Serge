import allure
import pytest


TEST_DATA = [
    {"name": "Test object 1", "color": "Green", "size": "Medium"},
    {"name": "Test object 2", "color": "Red", "size": "Small"},
    {"name": "Test object 3", "color": "Blue", "size": "Large"}
]


@allure.feature("Создание объекта")
@allure.story("Проверка создания объекта с параметрами")
@pytest.mark.critical
@pytest.mark.parametrize('data', TEST_DATA)
def test_create_post(data, create_post_endpoint):
    with allure.step("Формирование body запроса"):
        body = create_post_endpoint.build_body(
            name=data["name"],
            color=data["color"],
            size=data["size"]
        )

    response = create_post_endpoint.create_new_post(body=body, headers=None)
    create_post_endpoint.check_status_code_is_correct(response.status_code)


@allure.feature("Изменение объекта")
@allure.story("PUT изменение данных")
@pytest.mark.medium
def test_change_data_put(update_data_put, post_id):
    with allure.step("Формирование данных PUT запроса"):
        body = {
            "name": "Test object",
            "data": {
                "color": "Green",
                "size": "Large",
            }
        }
        response = update_data_put.make_changes_in_post(
            post_id=post_id, body=body, headers=None
            )
        update_data_put.check_status_code_is_correct(response.status_code)


@allure.feature("Изменение объекта")
@allure.story("PATCH частичное изменение данных")
def test_change_data_patch(update_data_patch, post_id):
    with allure.step("Формирование данных PATCH запроса"):
        body = {
            "data": {
                "color": "Red",
                "size": "Medium",
            }
        }
        response = update_data_patch.partial_changes_in_post(
            post_id=post_id, body=body, headers=None
            )
        update_data_patch.check_status_code_is_correct(response.status_code)


@allure.feature("Удаление объекта")
@allure.story("Проверка успешного удаления объекта")
@pytest.mark.high
def test_delete_object_successfully(delete_data, post_id):
    response = delete_data.delete_post(
            post_id=post_id, headers=None
        )
    delete_data.check_status_code_is_correct(response.status_code)
