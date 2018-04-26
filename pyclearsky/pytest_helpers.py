"""helpers for pytest"""
# taken from python's unit test
# may be covered by Python's license

from __future__ import print_function


def almostequal(first, second, places=7, verbose=True):
    # """Tests if two numbers are almost equal
    #
    # Used during unit testing with pytest
    #
    # """
    """Tests if two numbers are almost equal

    Used during unit testing with pytest

    Parameters
    ----------
    first : float/int
        first number can be a float or an int
    second : float/int
        second number can be a float or an int
    places : int
        if places is 1, it will check equality up to the first decimal place.
        Default places=7
    verbose : bool
        Will print details if first and second are not equal

    Returns
    -------
    bool
        Returns True it first and second are equal

    """
    if round(abs(second-first), places) != 0:
        if verbose:
            print(round(abs(second-first), places))
            print("notalmost: %s != %s" % (first, second))
        return False
    else:
        return True
