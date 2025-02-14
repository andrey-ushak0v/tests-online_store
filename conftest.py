import pytest
from selenium import webdriver
import requests
from config import BASE_URL, LOGIN, PASSWORD


@pytest.fixture()
def browser():
    """
    открывает главную страницу
    """
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.get(BASE_URL)
    yield chrome_browser
    chrome_browser.quit()


@pytest.fixture()
def login_session():
    """
    отправляет запрос в api на авторизацию,
    возвращает сессию
    """
    session = requests.Session()
    url = f"{BASE_URL}/auth/"
    payload = {
        "_controller_id": "1110558447",
        "referer": "%2F",
        "remember": "1",
        "login": LOGIN,
        "pass": PASSWORD
    }
    session.post(url, data=payload)
    return session


@pytest.fixture()
def authentication(login_session):
    """
    обновляет куки при открытии страницы
    после обновления страницы, пользователь авторизирован
    """
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.get(BASE_URL)
    chrome_browser.delete_all_cookies()
    for cookie in login_session.cookies:
        cookie_data = {
            "name": cookie.name,
            "value": cookie.value,
            "domain": cookie.domain if cookie.domain else "mega.readyscript.ru",
            "path": cookie.path if cookie.path else "/"
        }

        chrome_browser.add_cookie(cookie_data)
    chrome_browser.refresh()

    yield chrome_browser
    chrome_browser.quit()
