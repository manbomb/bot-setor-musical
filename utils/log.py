import logging
from unidecode import unidecode

logging.basicConfig(filename="errors.log")

def errorLog(msg) -> None:
    logging.error(unidecode(msg))

def errorLogUser(nome, email, grupo, comum) -> None:
    errorLog(f"{nome} - {email} - {grupo} - {comum}")