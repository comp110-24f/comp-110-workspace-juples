from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_edge():
    # test what happens if all of the ints in your list are odd.
    assert only_evens([1, 3, 5, 7, 9]) == []


def test_only_evens_even():
    # this function tests if a list of only even numbers will return a list of only even numbers
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_only_evens_evenandodd():
    # this function tests if a function with more even and odd numbers returns only even numbers
    assert only_evens([1, 2, 3, 4, 6]) == [2, 4, 6]


def test_sub_edge():
    # this edge case tests if the function will return an empty list when given an input list
    emptylist = []
    assert sub(lst=[], start=1, stop=1) == emptylist


def test_sub_units():
    # tests if the function returns list correct when given their respective indexs.
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_units2():
    # tests if the function returns proper list if the given indexes are outside of the index range of the list.
    a_list = [10, 20, 30, 40]
    assert sub(a_list, -1, 6) == a_list


def test_add_at_index_edge():
    # function to test what happens if you add to an empty list
    lst = []
    add_at_index(lst, 42, 0)
    assert lst == [42]


def test_add_at_index_unit1():
    # function to see if starting function at 0 works correctly
    lst = [1, 2, 3]
    add_at_index(lst, 10, 0)
    assert lst == [10, 1, 2, 3]


def test_add_at_index_unit2():
    # test if function works as intended
    lst = [1, 2, 3]
    add_at_index(lst, 10, 1)
    assert lst == [1, 10, 2, 3]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    list_3 = []
    with pytest.raises(IndexError):
        add_at_index(list_3, 1, 1)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
