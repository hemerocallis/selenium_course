import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    # далее следует код, который выполнится после завершения теста
    print("\nquit browser...")
    browser.quit()

class TestMainPage(object):
    # фикстура передается как параметр в метод
    def test_guest_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
