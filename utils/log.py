import logging
from unidecode import unidecode

logging.basicConfig(filename="errors.log")

def errorLog(msg) -> None:
    logging.error(unidecode(msg))