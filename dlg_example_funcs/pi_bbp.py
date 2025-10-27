"""
Functions for the calculation of PI to arbitrary precision.
"""

from decimal import Decimal
from decimal import getcontext


def pi_k(start_digit: int = 0, n_digits: int = 16, precision: int = 32) -> Decimal:
    """
    An implementation of the Bailey-Borwein-Plouffe function to
    calculate _n\_digits_ of PI starting at _start\_digit_.

    Parameters:
    -----------
    start_digit: int, first digit to calculate (default=0)
    n_digits: int, number of digits to calculate (default=16)
    precision: int, number of significant digits, if not provided defaults to
    start\_digit + n\_digits

    Returns:
    --------
    Decimal of n\_digits significant digits of PI

    """
    if start_digit < 0 or n_digits < 1:
        raise ValueError("Invalid value of start_digit or n_digits provided!")
    getcontext().prec = precision
    pi_digits = sum(
        1
        / Decimal(16) ** k
        * (
            Decimal(4) / (8 * k + 1)
            - Decimal(2) / (8 * k + 4)
            - Decimal(1) / (8 * k + 5)
            - Decimal(1) / (8 * k + 6)
        )
        for k in range(start_digit, start_digit + n_digits, 1)
    )

    return pi_digits


def decimal_sum(array: list, precision: int = 100, output=False) -> Decimal:
    """
    Sum an array of Decimals using the provided precision.

    Parameters:
    -----------
    array: list, array of numeric elements
    precision: int, precision of result, default 100
    output: bool, if True the result witll be printed, default False

    Returns:
    --------
    Decimal, the sum of array elements
    """
    getcontext().prec = precision
    dsum = sum(array)
    if output:
        print(f"{dsum:.{precision}}")
    return dsum


def generate_start_digits(precision: int = 10000, n_split: int = 10) -> range:
    """
    Generate the start\_digits range based on the anticipated _precision_ and number of
    splits (_n\_split_).

    Parameters:
    -----------
    precision: int, number of significant digits for decimal module
    n_split: int, number of start digits in the precision range.

    Returns:
    range object
    """
    return range(0, precision, int(precision / n_split))
