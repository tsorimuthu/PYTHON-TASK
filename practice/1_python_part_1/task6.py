"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    with open(filename) as opened_file:

     min_value = None
     max_value = None

    for line in opened_file:
        current_value = int(line.strip())

        if min_value is None or current_value< min_value:
            min_value = current_value

        if max_value is None or max_value < current_value:
            max_value = current_value
    return min_value,max_value

