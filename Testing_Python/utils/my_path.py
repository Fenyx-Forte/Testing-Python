import logging
from pathlib import Path

from Testing_Python.my_log import my_log

module_name = __name__.split(".")[-1]
logger = logging.getLogger(module_name)


@my_log.debug_log(logger)
def path(path: str) -> Path:
    return Path(path).resolve()
