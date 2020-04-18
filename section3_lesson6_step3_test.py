import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

expected_result = "Correct!"

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def answer():
    return str(math.log(int(time.time())))

@pytest.mark.parametrize('lesson_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_feedback(browser, lesson_id):
    link = f"https://stepik.org/lesson/{lesson_id}/step/1"
    browser.get(link)
    time.sleep(5)

    textarea_answer = browser.find_element(By.TAG_NAME, "textarea")
    answer_str = answer()
    textarea_answer.send_keys(answer_str)

    button_submit = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button_submit.click()
    time.sleep(5)

    pre_hint = browser.find_element(By.CSS_SELECTOR, "pre.smart-hints__hint")
    actual_result = pre_hint.text

    assert actual_result == expected_result, f"Expected '{expected_result}', got '{actual_result}'."
