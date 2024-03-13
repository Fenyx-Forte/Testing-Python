import logging

from Testing_Python.my_log import my_log
from Testing_Python.utils import my_path

module_name = __name__.split(".")[-1]
logger = logging.getLogger(module_name)


@my_log.debug_log(logger)
def read_file(path: str) -> str:
    path = my_path.path("teste.txt")

    content_file = ""
    with open(path) as f:
        logger.info("Lendo arquivo...")
        content_file = f.read()

    return content_file
