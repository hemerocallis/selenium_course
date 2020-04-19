from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    total = num1 + num2

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(total))

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
