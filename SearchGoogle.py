from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest
import time



@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get("https:/google.co.id")
    yield driver
    driver.quit()

def test_searchGoogle_myself(driver):
    driver.find_element(By.NAME, "q").send_keys("Wiranus Tegar" + Keys.ENTER)
    assert 'Wiranus Tegar' in driver.find_element(By.CSS_SELECTOR, "h3").text
    assert 'Wiranus Tegar' in driver.title


def test_searchGoogle_minji(driver):
    driver.find_element(By.NAME, "q").send_keys("minji" + Keys.ENTER)
    assert 'minji' in driver.find_element(By.CSS_SELECTOR, "h3").text
    assert 'minji' in driver.title
    


