def only_evens(lst: list[int]) -> int:
    empty = []
    newlist = []
    for x in lst:
        if x % 2 == 0:
            newlist.append(x)
    return newlist


def sub(lst: list[int], start: int, stop: int) -> list[int]:
    modlist = []
    if lst == modlist:
        return modlist
    if start < 0:
        start = 0
    if stop > len(lst):
        stop = len(lst)
    for x in range(start, stop):
        modlist.append(lst[x])

    return modlist


def add_at_index(lst: list[int], val: int, place: int) -> None:
    if place > len(lst) or place <= -1:
        raise IndexError("Index is out of bounds for the inout list")
    lst.insert(place, val)
