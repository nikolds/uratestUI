import pytest
import allure
import requests
from selenium import webdriver
from pom.homepage_nav import HomepageNav

@pytest.mark.usefixtures('setup')
@allure.feature('test_homepage')
@allure.story('статус')
def test_get_homepage():
    url = 'https://ura.news/'
    response = requests.get(url=url)
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

@pytest.mark.usefixtures('setup')
@allure.feature('test_nav_links')
@allure.story('Соответствие кнопок регионов')
class TestHomepage:
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        with allure.step('Навигационные кнопки регионов сотответствуют'):
            assert expected_links == actual_links, 'Validate nav links'






