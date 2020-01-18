from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    expected_result = "Congratulations! You have successfully registered!"
    browser = webdriver.Chrome()
    browser.get(link)

    # fill all required fields
    element1 = browser.find_element(By.XPATH, "//div[@class='form-group first_class']//input[1][@required]")
    element1.send_keys("пыщ")
    time.sleep(1)

    element2 = browser.find_element(By.XPATH, "//div[@class='form-group second_class']//input[1][@required]")
    element2.send_keys("пыщ")
    time.sleep(1)

    element3 = browser.find_element(By.XPATH, "//div[@class='form-group third_class']//input[1][@required]")
    element3.send_keys("пыщ")
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert expected_result == welcome_text

finally:
    time.sleep(10)
    browser.quit()
