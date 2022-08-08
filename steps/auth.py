import os
from time import sleep
from dotenv import load_dotenv
from selenium.webdriver.chrome.webdriver import WebDriver

from utils.selenium import check_exists_by_name, wait_element

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
USER = os.getenv('USER')
PASS = os.getenv('PASS')

def auth(driver: WebDriver) -> None:
    driver.get(BASE_URL)
    wait_element(
        lambda: check_exists_by_name(driver, 'login'),
        20,
        'Bloqueado no login!'
    )

    loginInput = driver.find_element_by_name('login')
    passInput = driver.find_element_by_name('password')
    buttonSubmit = driver.find_element_by_xpath('//button')

    loginInput.send_keys(USER)
    passInput.send_keys(PASS)
    sleep(1)
    buttonSubmit.click()

    print('passou')