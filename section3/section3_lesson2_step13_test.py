import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        expected_result = "Congratulations! You have successfully registered!"
        browser = webdriver.Chrome()
        browser.get(link)

        # fill all required fields
        element1 = browser.find_element(By.XPATH, "//div[@class='form-group first_class']//input[1][@required]")
        element1.send_keys("пыщ")

        element2 = browser.find_element(By.XPATH, "//div[@class='form-group second_class']//input[1][@required]")
        element2.send_keys("пыщ")

        element3 = browser.find_element(By.XPATH, "//div[@class='form-group third_class']//input[1][@required]")
        element3.send_keys("пыщ")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, expected_result, f"expected '{expected_result}', got '{welcome_text}'")
        browser.quit()


    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        expected_result = "Congratulations! You have successfully registered!"
        browser = webdriver.Chrome()
        browser.get(link)

        # fill all required fields
        element1 = browser.find_element(By.XPATH, "//div[@class='form-group first_class']//input[1][@required]")
        element1.send_keys("пыщ")

        element2 = browser.find_element(By.XPATH, "//div[@class='form-group second_class']//input[1][@required]")
        element2.send_keys("пыщ")

        element3 = browser.find_element(By.XPATH, "//div[@class='form-group third_class']//input[1][@required]")
        element3.send_keys("пыщ")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, expected_result, f"expected '{expected_result}', got '{welcome_text}'")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
