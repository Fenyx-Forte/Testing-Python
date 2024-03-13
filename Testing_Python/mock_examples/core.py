import os
from typing import Any

import requests

from Testing_Python.utils import my_path

PI = 3.14159


def area_of_circle(radius: float) -> float:
    """
    Function to calculate area of a cicle
    :param radius: Radius of the circle
    :return: Area of the circle
    """
    return PI * radius * radius


def make_file(filename: str) -> None:
    """
    Function to create a file
    :param filename: Name of the file to create
    :return: None
    """
    with open(my_path.path(filename), "w") as f:
        f.write("hello")


def remove_file(filename: str) -> None:
    """
    Function to remove a file
    :param filename: Name of the file to remove
    :return: None
    """
    os.remove(my_path.path(filename))


def get_yo_mamma_jokes() -> Any | None:
    """
    Function to get yo mamma jokes from an API
    :return: Response from the API
    """
    response = requests.get("https://api.yomomma.info/")
    return response.json()
