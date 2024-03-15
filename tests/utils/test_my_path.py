from pathlib import Path

from Testing_Python.utils import my_path


def test_path():
    """
    Test that the `path` function returns a `Path` object.

    This test verifies that the `my_path.path` function correctly returns a
    `Path` object representing the given path.

    Args:
        None

    Returns:
        None
    """
    assert (
        my_path.path('resources/resources/tests/test.txt')
        == Path('resources/resources/tests/test.txt').resolve()
    )
