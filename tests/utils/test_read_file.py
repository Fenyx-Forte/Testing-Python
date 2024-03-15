from Testing_Python.utils import read_file


def test_read_file():
    """
    This test ensures that the function `read_file.read_file` returns the
    content of the file specified.
    """
    assert read_file.read_file('resources/tests/test.txt') == '123'
