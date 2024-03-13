import logging

from Testing_Python.my_log import my_log

module_name = __name__.split(".")[-1]
logger = logging.getLogger(module_name)


@my_log.debug_log(logger)
def divide(a: int, b: int) -> float:
    """Return the result of a division operation between two numbers.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division operation.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        msg = f"You can't divide {a} by {b} because you can't divide by zero."
        logger.error(msg)
        raise ZeroDivisionError(msg)
