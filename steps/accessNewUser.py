import os
from time import sleep
from unicodedata import category
from dotenv import load_dotenv
from selenium.webdriver.chrome.webdriver import WebDriver


from utils.selenium import check_exists_by_name, wait_element, check_exists_by_xpath

load_dotenv()

BASE_URL = os.getenv('BASE_URL')

def accessNewUserPage(driver: WebDriver) -> None:
    driver.get(BASE_URL+'/painel')
    
    xpathCategory = "//span[text()='Preferências']"

    wait_element(
        lambda: check_exists_by_xpath(driver, xpathCategory),
        20,
        'Bloqueado na pagina de usuarios!'
    )

    categorySpan = driver.find_element_by_xpath(xpathCategory)
    categorySpan.click()

    sleep(2)
    
    categoryLi = categorySpan.find_element_by_xpath('./../..')
    categoryUl = categoryLi.find_element_by_xpath('./ul')
    subCategoryLis = list(categoryUl.find_elements_by_xpath('./li'))
    subCategoryLink = subCategoryLis[3].find_element_by_xpath('./a')
    subCategoryLink.click()

    xpathInlcuirButton = "//button[contains(@data-acao, 'incluir')]"

    wait_element(
        lambda: check_exists_by_xpath(driver, xpathInlcuirButton),
        20,
        'Bloqueado na pagina de usuarios!'
    )

    incluirButton = driver.find_element_by_xpath(xpathInlcuirButton)
    incluirButton.click()
    