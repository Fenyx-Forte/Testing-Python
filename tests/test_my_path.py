from pathlib import Path

from Testing_Python.utils import my_path


def test_path():
    """
    Test that path returns a Path object.
    """
    assert my_path.path("teste.txt") == Path("teste.txt").resolve()
