from selenium import webdriver
import csv

from options import set_chrome_options
from steps.accessNewUser import accessNewUserPage
from steps.auth import auth
from steps.fillWithUser import fillWithUser

capabilities = webdriver.DesiredCapabilities.CHROME
chrome_options = set_chrome_options()
driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities, executable_path='chromedriver.exe')

try:
    auth(driver)
except:
    print("Houve um erro na autenticação!")
    driver.quit()
    exit(1)

try:
    accessNewUserPage(driver)
except Exception as E:
    print("Houve um erro ao acessar página de usuários!")
    driver.quit()
    exit(1)

try:
    fillWithUser(driver, 'Sérgio Lucas Avilla da Silva', 'sergiolucasavilladasilva@gmail.com', 'ENCARREGADOS / SECRETÁRIOS', 'avenida')
except Exception as E:
    print("Houve um erro ao preencher/cadastrar usuário!")
    driver.quit()
    exit(1)

driver.quit()
exit(0)