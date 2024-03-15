import logging
from pathlib import Path

from Testing_Python.my_log import my_log

module_name = __name__.split('.')[-1]
logger = logging.getLogger(module_name)


@my_log.debug_log(logger)
def path(path: str) -> Path:
    """Resolves the provided path and returns a Path object.

    Args:
        path (str): The path to resolve.

    Returns:
        Path: A Path object representing the resolved path.
    """
    return Path(path).resolve()
