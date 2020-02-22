""" Bottom-Up Mergesort

!!Important!! it is a implementation to present the algorithm,
if you need to sort a list use list.sort for in place, or sorted
for a new list.
"""

from random import randint
from unittest import TestCase


def mergesort(arr: list):
    """ Sort a list using a bottom-up strategy

    Parameters
    ----------
    arr : list
    The array of numbers to be sorted

    Returns
    -------
    None
    """

    if len(arr) < 2:
        return

    length = len(arr)

    width = 1
    while width < length:

        for offset in range(0, length, width * 2):
            mid = min(offset + width, length)
            end = min(offset + 2 * width, length)

            merge(arr, offset, mid, end)

        width *= 2


def merge(arr: list, begin: int, middle: int, end: int):
    li = 0
    ri = 0

    left = arr[begin:middle]
    right = arr[middle:end]

    max_left = len(left)
    max_right = len(right)

    for i in range(begin, end):
        if li < max_left and (ri >= max_right or left[li] <= right[ri]):
            arr[i] = left[li]
            li += 1
        else:
            arr[i] = right[ri]
            ri += 1

##################
### Some Tests ###
##################


class TestBottomUpMergeSort(TestCase):

    def test_should_sort_empty(self):
        empty_list = []

        mergesort(empty_list)

        self.assertListEqual([], empty_list)

    def test_should_sort_single_element_list(self):
        single_list = [42]

        mergesort(single_list)

        self.assertListEqual([42], single_list)

    def test_should_sort_already_sorted_list(self):
        sorted_list = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]

        mergesort(sorted_list)

        self.assertListEqual([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], sorted_list)

    def test_should_sort_reverse_sorted_list(self):
        reversed_list = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2]

        mergesort(reversed_list)

        self.assertListEqual([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], reversed_list)

    def test_should_sort_not_sorted_list(self):
        not_sorted_list = [1, -1, 6, 2, 4, 3, 5, 0, 7, -2]

        mergesort(not_sorted_list)

        self.assertListEqual([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], not_sorted_list)

    def test_should_sort_random_list(self):
        random_size = randint(50, 100)
        random_list = [randint(-100, 100) for i in range(random_size)]

        mergesort(random_list)

        self.assertListEqual(sorted(random_list), random_list)
