import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait


LOCAL_URL = "http://localhost:5000/"


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.close()


def click_and_wait(driver, button, timeout=5):
    source = driver.page_source
    button.click()
    def compare_source(driver):
        try:
            return source != driver.page_source
        except WebDriverException:
            pass
    WebDriverWait(driver, timeout).until(compare_source)


def test_login_with_correct_credentials(driver):
    driver.get(LOCAL_URL)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.ID, "login_submit")

    username.send_keys("maria.k")
    password.send_keys("0227")
    button.click()

    WebDriverWait(driver, 1).until(lambda d: d.execute_script("return document.readyState") == "complete")
    assert driver.get_cookie("webonomicon") is not None


def test_login_with_correct_credentials_another_way(driver):
    driver.get(LOCAL_URL)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.ID, "login_submit")

    username.send_keys("maria.k")
    password.send_keys("0227")
    click_and_wait(driver, button)
    assert driver.get_cookie("webonomicon") is not None
