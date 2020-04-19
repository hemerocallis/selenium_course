from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//div[@class='form-group']//input[1][@required]")
    input1.send_keys("Liliya")

    input2 = browser.find_element(By.XPATH, "//div[@class='form-group']//input[2][@required]")
    input2.send_keys("Mir")

    input3 = browser.find_element(By.XPATH, "//div[@class='form-group']//input[3][@required]")
    input3.send_keys("hemera@mail.ru")

    file_uploader = browser.find_element(By.XPATH, "//input[@id='file']")
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'section2_lesson2_step8.txt')
    file_uploader.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
