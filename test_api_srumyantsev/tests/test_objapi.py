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
def test_create_object(data, create_object_endpoint):
    with allure.step("Формирование body запроса"):
        body = create_object_endpoint.build_body(
            name=data["name"],
            color=data["color"],
            size=data["size"]
        )

    response = create_object_endpoint.create_new_object(
        body=body, headers=None
    )
    create_object_endpoint.check_status_code_is_200(response.status_code)


@allure.feature("Изменение объекта")
@allure.story("PUT изменение данных")
@pytest.mark.medium
def test_change_data_put(update_data_put, object_id):
    with allure.step("Формирование данных PUT запроса"):
        body = {
            "name": "Test object",
            "data": {
                "color": "Green",
                "size": "Large",
            }
        }
        response = update_data_put.make_changes_in_object(
            object_id=object_id, body=body, headers=None
        )
        update_data_put.check_status_code_is_200(response.status_code)


@allure.feature("Изменение объекта")
@allure.story("PATCH частичное изменение данных")
def test_change_data_patch(update_data_patch, object_id):
    with allure.step("Формирование данных PATCH запроса"):
        body = {
            "data": {
                "color": "Red",
                "size": "Medium",
            }
        }
        response = update_data_patch.partial_changes_in_object(
            object_id=object_id, body=body, headers=None
        )
        update_data_patch.check_status_code_is_200(response.status_code)


@allure.feature("Удаление объекта")
@allure.story("Проверка успешного удаления объекта")
@pytest.mark.high
def test_delete_object_successfully(delete_data, object_id):
    response = delete_data.delete_object(
        object_id=object_id, headers=None
    )
    delete_data.check_status_code_is_200(response.status_code)
