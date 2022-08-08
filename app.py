from selenium import webdriver
from options import set_chrome_options

capabilities = webdriver.DesiredCapabilities.CHROME
chrome_options = set_chrome_options()
driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities, executable_path='chromedriver.exe')



driver.quit()