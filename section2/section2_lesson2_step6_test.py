from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    def scroll(element):
        browser.execute_script("return arguments[0].scrollIntoView(true);", element)

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_element = browser.find_element(By.ID, "answer")
    scroll(input_element)
    input_element.send_keys(y)

    checkbox_element = browser.find_element(By.ID, "robotCheckbox")
    scroll(checkbox_element)
    checkbox_element.click()

    radio_element = browser.find_element(By.ID, "robotsRule")
    scroll(radio_element)
    radio_element.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    scroll(submit_button)
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
