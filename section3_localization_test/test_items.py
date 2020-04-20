import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_localization(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(3)

    button_add = browser.find_element(By.XPATH, "//button[@type='submit' and @class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button_add != None, "There is no such element on the page."
