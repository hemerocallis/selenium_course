from selenium import webdriver
import time

enter_link = "https://www.labirint.ru/genres/2383/"
basket = "https://www.labirint.ru/cart/"

try:
    browser = webdriver.Chrome()
    browser.get(enter_link)

    button1 = browser.find_element_by_class_name("buy-link")
    button1.click()
    time.sleep(5)

    browser.get(basket)
    products = browser.find_elements_by_css_selector(".product-cart")

    assert len(products) == 1

finally:
    time.sleep(3)
    browser.quit()
