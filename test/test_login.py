from pages.base_actions import BasePage
import pytest
from locators import locators
from config import LOGIN, PASSWORD


class TestLogin:

    @pytest.fixture(autouse=True)
    def open_page_and_auth(self, browser):
        self.app = BasePage(browser)
    
    def test_login(self):
        self.app.click_button(locators.lk_button)
        self.app.click_button(locators.login_button)
        self.app.fill_in_field(locators.login_field, LOGIN)
        self.app.fill_in_field(locators.pass_field, PASSWORD)
        self.app.click_button(locators.submit_login_button)
        assert self.app.find_element_on_page_by_xpath(locators.name_account), 'логин провален'


