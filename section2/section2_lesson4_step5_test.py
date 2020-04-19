from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    # WebDriver будет искать каждый элемент в течение 5 секунт
    browser.implicitly_wait(5)

    browser.get(link)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    browser.quit()
