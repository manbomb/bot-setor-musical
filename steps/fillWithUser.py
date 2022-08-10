import json
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from utils.log import errorLog
from utils.selenium import check_exists_by_id, check_exists_by_name, wait_element

DEFAULT_PASS = 'setormusical'

def fillWithUser(driver: WebDriver, nome: str, email: str, grupo: str, comum: str) -> None:
    wait_element(
        lambda: check_exists_by_name(driver, 'nome'),
        20,
        'Bloqueado no preenchimento!'
    )

    nomeInput = driver.find_element_by_name('nome')
    nomeInput.send_keys(nome)

    loginInput = driver.find_element_by_name('login')
    emailInput = driver.find_element_by_name('email')
    loginInput.send_keys(email)
    emailInput.send_keys(email)

    senhaInput = driver.find_element_by_name('senha')
    confSenhaInput = driver.find_element_by_name('conf-senha')
    senhaInput.send_keys('setormusical')
    confSenhaInput.send_keys('setormusical')

    selectGrupo = Select(driver.find_element_by_name('id_grupo'))
    selectGrupoOptsTexts = list(map(lambda e: e.get_attribute('innerText').strip(), selectGrupo.options))
    selectGrupoOptsValues = list(map(lambda e: e.get_attribute('value'), selectGrupo.options))
    indexSelectedGroup = selectGrupoOptsTexts.index(grupo)
    valueSelectedGroup = selectGrupoOptsValues[indexSelectedGroup]

    selectGrupo.select_by_value(valueSelectedGroup)

    selectComum(driver, comum)

    driver.execute_script("enviarForm('usuario', 'salvar')")

    try:
        verificaHouveErro(driver)    
    except Exception as E:
        errorLog(f"{nome} - {email} - {grupo} - {comum}")
        raise E

def selectComum(driver: WebDriver, comum: str) -> None:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(f'https://musical.congregacao.org.br/igrejas/filtra_igreja_setor?q={comum} maringa')
    jsonData = driver.find_element_by_tag_name('body').get_attribute('innerText')

    arrayIgrejas = json.loads(jsonData)
    idIgreja = arrayIgrejas[0]['id']
    nomeIgreja = arrayIgrejas[0]['text']

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    script = f'const option = document.createElement("option");option.value = "{idIgreja}";option.innerText = "{nomeIgreja}";option.selected = true;document.querySelector("#id_igreja").appendChild(option);'
    driver.execute_script(script)

def verificaHouveErro(driver: WebDriver) -> None:
    driver.implicitly_wait(3)
    if check_exists_by_id(driver, 'alerta-msg'):
        raise Exception("Houve um erro ao tentar cadastrar este usuário!")