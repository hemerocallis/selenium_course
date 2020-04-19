import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture()
def browser():
    print("\nstart browser...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print("\npreparing some critical data for every test")

class TestMainPage():

    def test_guest_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
