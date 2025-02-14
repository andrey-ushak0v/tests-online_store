from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browserr):
        self.driver = browserr
        self.actions = ActionChains(self.driver)

    def open_page(self, url):
        """открывает страницу"""
        self.driver.get(url)

    def find_element_on_page_by_xpath(self, locator, timeout=10):
        """ищет элемент по xpath используя ожидание"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

    def click_button(self, locator):
        """кликает по кнопке"""
        button = self.find_element_on_page_by_xpath(locator)
        self.driver.execute_script("arguments[0].click();", button)

    def fill_in_field(self, locator, text, timeout=10):
        """заполняет поле ввода предварительно отчистив его"""
        field = self.find_element_on_page_by_xpath(locator, timeout)
        field.clear()
        field.send_keys(text)

    def move_mouse_to_element(self, locator):
        """наводит мышь на элемент"""
        elem = self.find_element_on_page_by_xpath(locator, timeout=10)
        self.actions.move_to_element(elem).perform()

    def get_element_text(self, locator):
        """получает текст из элемента"""
        return self.find_element_on_page_by_xpath(locator).text
