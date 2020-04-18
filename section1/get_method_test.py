import time
from selenium import webdriver

def submit(element):
    element.click()
    time.sleep(5)

driver = webdriver.Chrome()
time.sleep(5) # wait 5 sec

driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

textarea = driver.find_element_by_css_selector(".textarea")
time.sleep(5)

textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element_by_css_selector(".submit-submission")
submit(submit_button)

again_button = driver.find_element_by_css_selector(".again-btn")
submit(again_button)

textarea = driver.find_element_by_css_selector(".textarea")
textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element_by_css_selector(".submit-submission")
submit(submit_button)

driver.quit()
