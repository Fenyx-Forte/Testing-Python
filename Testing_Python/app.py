import logging

from Testing_Python.my_log import my_log
from Testing_Python.utils import read_file

module_name = __name__.split(".")[-1]
logger = logging.getLogger(module_name)


@my_log.debug_log(logger)
def main() -> None:
    content_file = read_file.read_file("teste.txt")

    logger.info(f"Conteudo do arquivo: {content_file}")
