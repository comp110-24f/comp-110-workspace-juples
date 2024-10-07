"""Mutating functions."""

__author__ = "730511752"


def manual_append(listchange: list[int], numchange: int) -> None:
    listchange.append(numchange)




list_1: list[int] = [1,2,3]

list_2 = list_1

def double(listchange: list[int]) -> None:
    length = len(listchange)
    x = 0 
    while x < length:
        newval = listchange[x] * 2
        listchange[x] = newval
        x += 1
        print(list_1)
        print(list_2)
