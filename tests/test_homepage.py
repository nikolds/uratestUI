import pytest
import allure
import requests


@pytest.mark.usefixtures('setup')
class TestHomepage:
    def test_homepage(self):
        pass


@pytest.mark.usefixtures('setup')
@allure.feature('test_homepage')
@allure.story('Получение фото случайной собаки и вложенные друг в друга шаги')
def test_get_homepage():
    url = 'https://ura.news/'
    response = requests.get(url=url)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    pass
