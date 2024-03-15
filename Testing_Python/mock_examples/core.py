import os
from typing import Any

import requests

from Testing_Python.utils import my_path

PI = 3.14159


def area_of_circle(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return PI * radius * radius


def make_file(filename: str) -> None:
    """
    Create a file with the given filename.

    Args:
        filename (str): The name of the file to be created.

    Returns:
        None: This function does not return anything.
    """
    with open(my_path.path(filename), 'w') as f:
        f.write('hello')


def remove_file(filename: str) -> None:
    """
    Remove a file.

    Args:
        filename (str): The name of the file to remove.

    Returns:
        None: This function does not return anything.
    """
    os.remove(my_path.path(filename))


def get_yo_mamma_jokes() -> Any | None:
    """
    Retrieves a joke from the Yo Mamma API.

    Returns:
        Union[dict, None]: A dictionary containing a joke, if successful.
                          If the request fails, returns None.
    """
    response = requests.get('https://api.yomomma.info/')
    return response.json()
