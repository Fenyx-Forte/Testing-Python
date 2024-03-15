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
    mocker.patch('Testing_Python.mock_examples.core.PI', 3.0)
    assert core.area_of_circle(10) == 300.0


def test_make_file():
    """
    Test the function `make_file` to verify that it creates a file with the
    given filename.

    This function takes no parameters.

    Returns:
        None. This function does not return anything.
    """
    core.make_file(filename='delete_me.txt')
    assert os.path.isfile('delete_me.txt')


def test_make_file_with_mock(mocker):
    """
    Test the function `make_file` with mock to verify that it creates a
    file with the given filename.

    This test function takes a single parameter `mocker`, which is a fixture
    provided by `pytest-mock` for mocking objects.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The pytest-mock fixture for
            mocking objects.

    Returns:
        None: This function does not return anything.
    """
    filename = 'delete_me.txt'

    # Mock the 'open' function call to return a file object.
    mock_file = mocker.mock_open()
    mocker.patch('builtins.open', mock_file)

    # Call the function that creates the file.
    core.make_file(filename)

    # Assert that the 'open' function was called with the expected arguments.
    mock_file.assert_called_once_with(my_path.path(filename), 'w')

    # Assert that the file was written to with the expected text.
    mock_file().write.assert_called_once_with('hello')


def test_remove_file():
    """
    Test the `remove_file` function to verify that it removes the file with the
    given filename.

    This function takes no parameters.

    Returns:
        None. This function does not return anything.
    """
    core.make_file(filename='delete_me.txt')
    core.remove_file(filename='delete_me.txt')
    assert not os.path.isfile('delete_me.txt')


def test_get_yo_mamma_jokes_with_mock(mocker):
    """
    Test the 'get_yo_mamma_jokes' function by mocking the 'requests.get'
    function.

    This test function mocks the 'requests.get' function to return a mocked
    response. The mocked response is configured to return a JSON response with
    a specific joke. The function then calls 'get_yo_mamma_jokes' and asserts
    that the returned joke matches the expected joke.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The pytest-mock fixture for
            mocking objects.

    Returns:
        None: This function does not return anything.
    """
    mock_response = {
        'joke': 'Yo mamma so ugly she made One Direction go another direction.'
    }

    # mock the requests.get function
    mocker.patch(
        'Testing_Python.mock_examples.core.requests.get'
    ).return_value.json.return_value = mock_response

    response = core.get_yo_mamma_jokes()

    # check that requests.get was called with the correct URL
    requests.get.assert_called_once_with('https://api.yomomma.info/')

    # check that the result is the expected mock response
    assert response == mock_response
