import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


LOCAL_URL = "http://localhost:5000/"


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.close()


def test_home_page_title(driver):
    driver.get(LOCAL_URL)
    heading = driver.find_element(By.CSS_SELECTOR, "h1")
    assert heading.text == "Staff and Experiments"


def test_home_page_initially_no_experiments(driver):
    driver.get(LOCAL_URL)
    div = driver.find_element(By.ID, "experiments")
    assert len(div.find_elements(By.CSS_SELECTOR, "*")) == 0
