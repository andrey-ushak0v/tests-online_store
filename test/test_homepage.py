import pytest
from pages.base_actions import BasePage
from locators import locators


class TestHomepage:

    @pytest.fixture(autouse=True)
    def open_homepage_with_auth(self, authentication):
        """открывает главную страницу под авторизацией"""
        self.app = BasePage(authentication)

    def test_product_display_in_the_catalog(self):
        """
        тест проверяющий работу меню каталога и отображения товара
        шаги:
        1) кликнуть по кнопке каталога
        2) навести курсор на категорию "Электроника"
        3) навести курсор на подкатегорию "планшеты"
        4) кликнуть по бренду "Digma"
        5) проверить что нужный элемент отображается
        """
        self.app.click_button(locators.catalog_button)
        self.app.move_mouse_to_element(locators.electronic_category)
        self.app.move_mouse_to_element(locators.planshety_categoty)
        self.app.click_button(locators.digma_category)
        assert (self.app.find_element_on_page_by_xpath(locators.planshet),'товар не отображается')

