import pytest

from Testing_Python.utils import user


@pytest.fixture
def my_user() -> user.User:
    """
    Pytest fixture to create a User instance for testing.

    Returns:
        user.User: A User instance with id 1, name "John Doe", and age 30.
    """
    return user.User(1, 'John Doe', 30)


def test_user_creation(my_user: user.User) -> None:
    """Test the creation of a User instance.

    This test verifies that a User object is correctly initialized with the
    provided id, name, and age.

    Args:
        my_user (user.User): The User object to be tested.

    Returns:
        None
    """
    assert my_user.id == 1
    assert my_user.name == 'John Doe'
    assert my_user.age == 30


def test_greet(my_user: user.User) -> None:
    """Test the greet method of a User instance.

    This test verifies that the greet method of a User object returns a
    properly formatted greeting message.

    Args:
        my_user (user.User): The User object to be tested.

    Returns:
        None
    """
    greeting: str = my_user.greet()
    assert greeting == 'Hello, my name is John Doe and I am 30 years old.'
