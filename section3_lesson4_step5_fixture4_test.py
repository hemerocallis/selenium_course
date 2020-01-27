import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="class") # scope="function" / "module" / "session"
def browser():
    print("\nstart browser...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()

class TestMainPage():

    def test_guest_see_login_link(self, browser):
        print("\nstart test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("\nfinish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("\nstart test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("\nfinish test2")
