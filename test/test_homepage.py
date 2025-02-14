from pages.base_actions import BasePage
import pytest
from locators import locators


class TestHomepage:

    @pytest.fixture(autouse=True)
    def open_homepage_with_auth(self, authentication):
        self.app = BasePage(authentication)

    def test_product_display_in_the_catalog(self):
        self.app.click_button(locators.catalog_button)
        self.app.move_mouse_to_elemet(locators.electronic_category)
        self.app.move_mouse_to_elemet(locators.planshety_categoty)
        self.app.click_button(locators.digma_category)
        self.app.find_element_on_page_by_xpath(locators.planshet)
        assert self.app.find_element_on_page_by_xpath(locators.planshet), 'товар не отображается'

