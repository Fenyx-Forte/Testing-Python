import pytest

from Testing_Python.utils import user


@pytest.fixture
def my_user() -> user.User:
    """
    Pytest fixture to create a User instance for testing.
    """
    return user.User(1, "John Doe", 30)


def test_user_creation(my_user: user.User) -> None:
    """
    Test the creation of a User instance.
    """
    assert my_user.id == 1
    assert my_user.name == "John Doe"
    assert my_user.age == 30


def test_greet(my_user: user.User) -> None:
    """
    Test the greet method of a User instance.
    """
    greeting: str = my_user.greet()
    assert greeting == "Hello, my name is John Doe and I am 30 years old."
