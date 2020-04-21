from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_guest_can_see_btn_add_to_busket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(3)

    locator = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    button_add = WebDriverWait(browser, 30).until(EC.visibility_of_element_located(locator), "Button is not found.")
    assert button_add, "There is no such element on the page."
