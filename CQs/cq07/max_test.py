from CQs.cq07.find_max import find_and_remove_max

lst = [1, 2, 3, 4]


def test_return_max_value():
    assert find_and_remove_max(lst) == 4


def test_mutates_input():
    newlist = [1, 2, 3]
    assert find_and_remove_max(lst) == newlist


def test_empty_list():
    data = []
    assert find_and_remove_max(data) == -1
