import allure


class Endpoint:
    def __init__(self, base_url):
        self.url = base_url
    response = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Проверка кода ответа')
    def check_status_code_is_200(self):
        assert self.status_code == 200

    @property
    def status_code(self):
        if self.response:
            return self.response.status_code
        return None
