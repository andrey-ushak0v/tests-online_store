import pytest
from pages.base_page import BasePage
from locators.login_locators import LogInLocators
from config import LOGIN, PASSWORD


class TestLogin:

    @pytest.fixture(autouse=True)
    def open_page_login(self, browser):
        """открывает главную страницу без авторизации"""
        self.app = BasePage(browser)

    def test_login(self):
        """
        проверяет авторизацию
        шаги:
        1) кликнуть по нопке "Личный кабинет"
        2) кликнуть по кнопке "Вход"
        3) заполнить поле "Логин"
        4) заполнить поле "пароль"
        5) кликнуть по кнопке вход
        6) проверить что имя пользователя отображается после авторизации
        """
        self.app.click_button(LogInLocators.lk_button)
        self.app.click_button(LogInLocators.login_button)
        self.app.fill_in_field(LogInLocators.login_field, LOGIN)
        self.app.fill_in_field(LogInLocators.pass_field, PASSWORD)
        self.app.click_button(LogInLocators.submit_login_button)
        assert self.app.find_element_on_page_by_xpath(
            LogInLocators.name_account), 'логин провален'
