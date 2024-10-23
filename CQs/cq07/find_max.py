def find_and_remove_max(lst: list[int]) -> int:
    if not lst:
        return -1
    max_value = max(lst)
    lst[:] = [x for x in lst if x != max_value]
    return max_value
