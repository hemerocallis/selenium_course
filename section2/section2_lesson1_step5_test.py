from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_element = browser.find_element(By.ID, "answer")
    input_element.send_keys(y)
    checkbox_element = browser.find_element(By.ID, "robotCheckbox")
    checkbox_element.click()
    radio_element = browser.find_element(By.ID, "robotsRule")
    radio_element.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
