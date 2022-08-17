from time import sleep
from selenium import webdriver
import csv

from options import set_chrome_options
from steps.accessNewUser import accessNewUserPage
from steps.auth import auth
from steps.fillWithUser import fillWithUser
from steps.readCsv import readCsv
from utils.log import errorLogUser

users = readCsv('./data.csv')

capabilities = webdriver.DesiredCapabilities.CHROME
chrome_options = set_chrome_options()
driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities, executable_path='chromedriver.exe')

try:
    auth(driver)
except:
    print("Houve um erro na autenticação!")
    driver.quit()
    exit(1)


for user in users:
    try:
        accessNewUserPage(driver)
    except Exception as E:
        print("Houve um erro ao acessar página de usuários!")
        driver.quit()
        exit(1)
    try:
        fillWithUser(driver, **user)
        sleep(3)
        accessNewUserPage(driver)
    except Exception as E:
        errorLogUser(**user)
        print("Houve um erro ao preencher/cadastrar usuário!")

driver.quit()
exit(0)