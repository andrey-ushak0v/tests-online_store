import pytest
from pages.base_page import BasePage
from locators.homepage_locators import HomePageLocators


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
        self.app.click_button(HomePageLocators.catalog_button)
        self.app.move_mouse_to_element(HomePageLocators.electronic_category)
        self.app.move_mouse_to_element(HomePageLocators.planshety_categoty)
        self.app.click_button(HomePageLocators.digma_category)
        assert self.app.find_element_on_page_by_xpath(
            HomePageLocators.planshet), 'товар не отображается'
