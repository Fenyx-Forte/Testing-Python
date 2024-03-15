import pytest

from Testing_Python.utils import math_utils


def test_divide_positive_numbers() -> None:
    """Test that divide returns the correct result when given two positive
    numbers.

    Args:
        None

    Returns:
        None
    """
    result = math_utils.divide(1, 2)

    assert result == 0.5


def test_divide_negative_numbers() -> None:
    """Test that divide returns the correct result when given at least one
    negative number.

    Args:
        None

    Returns:
        None
    """
    assert math_utils.divide(5, -2) == -2.5
    assert math_utils.divide(-2, 5) == -0.4
    assert math_utils.divide(-2, -5) == 0.4


@pytest.mark.parametrize(
    'a, b, expected', [
    (5, -2, -2.5),
    (-2, 5, -0.4),
    (-2, -5, 0.4)
])
def test_divide_negative_numbers_version_2(a, b, expected) -> None:
    """Test that divide returns the correct result when given at least one
    negative number.

    Args:
        a (int): The numerator.
        b (int): The denominator.
        expected (float): The expected result of the division.

    Returns:
        None
    """
    assert math_utils.divide(a, b) == expected


def test_divide_by_zero() -> None:
    """Test that divide raises an error when dividing by zero.

    Args:
        None

    Returns:
        None
    """
    with pytest.raises(ZeroDivisionError):
        math_utils.divide(1, 0)
