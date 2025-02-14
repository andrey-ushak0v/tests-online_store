from pages.base_actions import BasePage
import pytest
from locators import locators
from config import BASE_URL

class TestProduct:

    @pytest.fixture(autouse=True)
    def open_product_with_auth(self, authentication):
        self.app = BasePage(authentication)
        self.app.open_page(f"{BASE_URL}/catalog/digma/")

    def test_add_to_card_and_delete(self):
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
        self.app.click_button(locators.product_card)    
        product_title = self.app.get_element_text(locators.text_planshet)
        self.app.click_button(locators.add_to_favorites_button)
        self.app.click_button(locators.to_favorite_button)
        title_product_in_favorite = self.app.get_element_text(locators.product_in_favorite)
        assert product_title == title_product_in_favorite, 'товар не добавился'
        self.app.click_button(locators.delete_from_favorite)
        assert self.app.find_element_on_page_by_xpath(locators.empty_fav), 'товар не удалился'