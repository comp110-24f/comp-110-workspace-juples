"""challenge question trying out different kind of loops"""

__author__ = "730511752"


def w_sum(vals: list[float]) -> float:
    total = 0.0
    index = 0

    while index < len(vals):
        total += vals[index]
        index += 1

    return total


def f_sum(vals: list[float]) -> float:
    total = 0.0
    i = 0
    for n in vals:
        total += vals[i]
        i += 1
    return total


def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for n in range(0, len(vals)):
        total += vals[n]
    return total
