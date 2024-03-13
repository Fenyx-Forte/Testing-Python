import os

import requests

from Testing_Python.mock_examples import core
from Testing_Python.utils import my_path


def test_area_of_circle() -> None:
    """
    Test that area_of_circle returns the correct result.
    """
    assert core.area_of_circle(10) == 314.159


# Mock a variable or constant
def test_area_of_circle_with_mock(mocker) -> None:
    """
    Test that area_of_circle returns the correct result with mock.
    """
    mocker.patch("Testing_Python.mock_examples.core.PI", 3.0)
    assert core.area_of_circle(10) == 300.0


def test_make_file():
    """
    Function to test make file
    :return: None
    """
    core.make_file(filename="delete_me.txt")
    assert os.path.isfile("delete_me.txt")


def test_make_file_with_mock(mocker):
    """
    Function to test make file with mock
    :param mocker: pytest-mock fixture
    :return: None
    """
    filename = "delete_me.txt"

    # Mock the 'open' function call to return a file object.
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)

    # Call the function that creates the file.
    core.make_file(filename)

    # Assert that the 'open' function was called with the expected arguments.
    mock_file.assert_called_once_with(my_path.path(filename), "w")

    # Assert that the file was written to with the expected text.
    mock_file().write.assert_called_once_with("hello")


def test_remove_file():
    """
    Function to test remove file
    :return: None
    """
    core.make_file(filename="delete_me.txt")
    core.remove_file(filename="delete_me.txt")
    assert not os.path.isfile("delete_me.txt")


def test_get_yo_mamma_jokes_with_mock(mocker):
    """
    Function to test get yo mamma jokes with mock
    """
    mock_response = {
        "joke": "Yo mamma so ugly she made One Direction go another direction."
    }

    # mock the requests.get function
    mocker.patch(
        "Testing_Python.mock_examples.core.requests.get"  
    ).return_value.json.return_value=mock_response

    response = core.get_yo_mamma_jokes()

    # check that requests.get was called with the correct URL
    requests.get.assert_called_once_with("https://api.yomomma.info/")

    # check that the result is the expected mock response
    assert response == mock_response
