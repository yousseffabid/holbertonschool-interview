#!/usr/bin/python3
"""Minoperations function"""


def minOperations(n):
    """ Calculates the fewest number of operations needed
        to result in exactly n H characters in the file

        Args:
            n: repetitions of H

        Returns:
            number of operations (Copy & Paste) to reach n Hs
    """
    total = 1
    operations = 0
    carrier = 0

    while total < n:
        if n % total == 0:
            carrier = total
            total *= 2
            operations += 1
        else:
            total += carrier
        operations += 1

    return operations
