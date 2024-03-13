from Testing_Python.utils import read_file


def test_read_file():
    """
    Test that read_file returns the content of the file.
    """
    assert read_file.read_file("teste.txt") == "123"
