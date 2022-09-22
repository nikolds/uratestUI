from base.Selenium_Base import Selenium_Base
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class HomepageNav(Selenium_Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '//*[@id="header"]/div/div[1]/div[1]/ul'
        self.NAV_LINK_TEXT = ['ВСЕ РЕГИОНЫ\nМОСКОВСКАЯ ОБЛ.\nСВЕРДЛОВСКАЯ ОБЛ.\nЧЕЛЯБИНСКАЯ ОБЛ.\nКУРГАНСКАЯ ОБЛ.\nТЮМЕНСКАЯ ОБЛ.\nЮГРА\nЯМАЛ\nПЕРМСКИЙ КРАЙ']

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('xpath', self.__nav_links, 'Header Navigation links')

    def get_nav_links_text(self) -> list[str]:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return nav_links_text
