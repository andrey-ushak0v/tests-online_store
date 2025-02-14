import pytest
from locators import locators
from config import BASE_URL
from pages.base_actions import BasePage


class TestProduct:

    @pytest.fixture(autouse=True)
    def open_product_with_auth(self, authentication):
        """открывает страницу с планшетами, под авторизацией"""
        self.app = BasePage(authentication)
        self.app.open_page(f"{BASE_URL}/catalog/digma/")

    def test_add_to_card_and_delete(self):
        """
        проверяет корректность добавления
        товара в корзину и удаления из нее
        шаги: 
        1) открыть карточку тоовара
        2) получить текст названия товара
        3) кликнуть по канопке "Добавить в корзину"
        4) перейти в козину
        5) получить название товара отображаемого в корзине
        6) сравить названия
        7) нажать кнопку нажать кнопку отчистки корзины (редирект на главную)
        8) нажать кнопку перехода в корзину
        9) проверить наличие текста "корзина пуста"
        """
        self.app.click_button(locators.product_card)   
        product_title = self.app.get_element_text(locators.text_planshet)
        self.app.click_button(locators.add_to_card_button)
        self.app.click_button(locators.to_cart)
        title_product_in_card = self.app.get_element_text(locators.product_in_card)
        assert product_title == title_product_in_card, 'товар не добавился'
        self.app.click_button(locators.clear_cart_button)
        self.app.click_button(locators.card_button_from_home)
        assert self.app.find_element_on_page_by_xpath(locators.empty_cart), 'товар не удалился'

    def test_add_to_favorites_and_delete(self):
        """
        проверяет корректность добавления
        товара в избранное и удаления из избранного
        шаги: 
        1) открыть карточку тоовара
        2) получить текст названия товара
        3) кликнуть по канопке "Добавить в избранное"
        4) перейти в избранное
        5) получить название товара отображаемого в избранное
        6) сравить названия
        7) нажать кнопку убирания из избранного (сердечко рядом с товаром)
        8) проверить наличие текста "Нет товаров в избранном"
        """
        self.app.click_button(locators.product_card)    
        product_title = self.app.get_element_text(locators.text_planshet)
        self.app.click_button(locators.add_to_favorites_button)
        self.app.click_button(locators.to_favorite_button)
        title_product_in_favorite = self.app.get_element_text(locators.product_in_favorite)
        assert product_title == title_product_in_favorite, 'товар не добавился'
        self.app.click_button(locators.delete_from_favorite)
        assert self.app.find_element_on_page_by_xpath(locators.empty_fav), 'товар не удалился'