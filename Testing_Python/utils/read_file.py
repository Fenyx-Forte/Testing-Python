import logging

from Testing_Python.my_log import my_log
from Testing_Python.utils import my_path

module_name = __name__.split('.')[-1]
logger = logging.getLogger(module_name)


@my_log.debug_log(logger)


def read_file(file_path: str) -> str:
    """Reads the content of a file given its path.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file.
    """
    path = my_path.path(file_path)

    content_file = ''
    with open(path) as f:
        logger.info('Reading file...')
        content_file = f.read()

    return content_file
