from time import sleep
from typing import Callable
from selenium.common.exceptions import NoSuchElementException

def check_exists_by_name(webdriver, name):
    try:
        webdriver.find_element_by_name(name)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_xpath(webdriver, xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def wait_element(cond: Callable, to: int, errorMessage: str, errorCond: Callable=lambda: False):
    attemps = 0
    while not cond():
        if attemps > to or errorCond():
            raise Exception(errorMessage)
        attemps += 1
        sleep(1)