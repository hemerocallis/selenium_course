from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    expected_result = "Congratulations! You have successfully registered!"
    browser = webdriver.Chrome()
    browser.get(link)

    # fill all required fields
    elements = browser.find_elements(By.CSS_SELECTOR, "[required]")
    for element in elements:
        element.send_keys("пыщ")
        time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert expected_result == welcome_text
    assert len(elements) == 3

finally:
    time.sleep(10)
    browser.quit()
