"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    result = []
    prev_power = 0

    for num in ints :
        power = num ** 2
        result.append(power- (prev_power**2 -prev_power))
        prev_power=num
    return result
print(calculate_power_with_difference([1,2,3]))
