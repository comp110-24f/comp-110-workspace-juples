"""this my third challenge question for comp 110"""

__author__ = "730511752"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        char = phrase[index]

        if char == search_char:
            count = count + 1

        index = index + 1

    return count
