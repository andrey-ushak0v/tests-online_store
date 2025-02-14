import pytest
from locators.productpage_locators import ProductPageLocators
from config import BASE_URL
from pages.base_page import BasePage


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
        self.app.click_button(ProductPageLocators.product_card)   
        product_title = self.app.get_element_text(
            ProductPageLocators.text_planshet
            )
        self.app.click_button(ProductPageLocators.add_to_card_button)
        self.app.click_button(ProductPageLocators.to_cart)
        title_product_in_card = self.app.get_element_text(
            ProductPageLocators.product_in_cart)
        assert product_title == title_product_in_card, 'товар не добавился'
        self.app.click_button(ProductPageLocators.clear_cart_button)
        self.app.click_button(ProductPageLocators.card_button_from_home)
        assert self.app.find_element_on_page_by_xpath(
            ProductPageLocators.empty_cart), 'товар не удалился'

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
        self.app.click_button(ProductPageLocators.product_card)    
        product_title = self.app.get_element_text(
            ProductPageLocators.text_planshet)
        self.app.click_button(ProductPageLocators.add_to_favorites_button)
        self.app.click_button(ProductPageLocators.to_favorites_button)
        title_product_in_favorite = self.app.get_element_text(
            ProductPageLocators.product_in_favorites)
        assert product_title == title_product_in_favorite, 'товар не добавился'
        self.app.click_button(ProductPageLocators.delete_from_favorites)
        assert self.app.find_element_on_page_by_xpath(
            ProductPageLocators.empty_favorites), 'товар не удалился'
