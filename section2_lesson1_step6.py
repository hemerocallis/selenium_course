from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(3)

    checkbox_element = browser.find_element(By.ID, "robotCheckbox")
    checkbox_element_checked = checkbox_element.get_attribute("checked")
    print("Default value of robot checkbox: ", checkbox_element_checked)

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("Default value of people radiobutton: ", people_checked)

    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_checked = robot_radio.get_attribute("checked")
    print("Default value of robot radiobutton: ", robot_checked)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_disabled_default = submit_button.get_attribute("disabled")
    print("Default value of submit button's disabled attribute: ", submit_disabled_default)

    time.sleep(9)
    submit_disabled_overtime = submit_button.get_attribute("disabled")
    print("Value of submit button's disabled attribute whem time is up: ", submit_disabled_overtime)

    assert checkbox_element_checked is None, "Robot checkbox is selected by default."
    assert people_checked == "true", "People radio is not selected by default."
    assert robot_checked is None, "Robot radio is selected by default."
    assert submit_disabled_default is None, "Submit is disabled by default."
    assert submit_disabled_overtime is not None, "Submit is enabled when time is up."

finally:
    browser.quit()
