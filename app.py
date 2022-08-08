from selenium import webdriver

from options import set_chrome_options
from steps.accessNewUser import accessNewUserPage
from steps.auth import auth

capabilities = webdriver.DesiredCapabilities.CHROME
chrome_options = set_chrome_options()
driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities, executable_path='chromedriver.exe')

try:
    auth(driver)
except:
    print("Houve um erro na autenticação!")
    exit(1)
    driver.quit()

try:
    accessNewUserPage(driver)
except Exception as E:
    print("Houve um erro ao acessar página de usuários!")
    print(E)
    exit(1)
    driver.quit()

driver.quit()
exit(0)