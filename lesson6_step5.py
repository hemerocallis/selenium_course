from selenium import webdriver
import time
import math

link1 = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link1)

    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link2 = browser.find_element_by_link_text(link_text)
    link2.click()

    input1 = browser.find_element_by_tag_name(".form-group input:nth-child(2)")
    input1.send_keys("Liliya")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Mirgayazova")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Krasnoyarsk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
