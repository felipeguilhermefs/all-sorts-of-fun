""" Quicksort (Lomuto pivot strategy)

!!Important!! it is a implementation to present the algorithm,
if you need to sort a list use list.sort for in place, or sorted
for a new list.
"""

from random import randint
from unittest import TestCase


def quicksort(arr: list) -> list:
    __quicksort(arr, 0, len(arr) - 1)


def __quicksort(arr: list, low: int, high: int):
    if high - low < 1:
        return

    pivot_index = __partition(arr, low, high)

    __quicksort(arr, low, pivot_index - 1)
    __quicksort(arr, pivot_index + 1, high)


def __partition(arr: list, low: int, high: int) -> int:
    # In Lomuto strategy the last element of the segment is chosen
    pivot_index = high
    pivot = arr[pivot_index]
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[pivot_index], arr[i] = arr[i], arr[pivot_index]

    return i


##################
### Some Tests ###
##################


class TestLomutoQuickSort(TestCase):

    def test_should_sort_empty(self):
        empty_list = []

        quicksort(empty_list)

        self.assertListEqual([], empty_list)

    def test_should_sort_single_element_list(self):
        single_list = [42]

        quicksort(single_list)

        self.assertListEqual([42], single_list)

    def test_should_sort_already_sorted_list(self):
        sorted_list = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]

        quicksort(sorted_list)

        self.assertListEqual([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], sorted_list)

    def test_should_sort_reverse_sorted_list(self):
        reversed_list = [7, 6, 5, 4, 3, 2, 1, 0, -1, -2]

        quicksort(reversed_list)

        self.assertListEqual([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], reversed_list)

    def test_should_sort_not_sorted_list(self):
        not_sorted_list = [1, -1, 6, 2, 4, 3, 5, 0, 7, -2]

        quicksort(not_sorted_list)

        self.assertListEqual([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7], not_sorted_list)

    def test_should_sort_random_list(self):
        random_size = randint(50, 100)
        random_list = [randint(-100, 100) for i in range(random_size)]

        quicksort(random_list)

        self.assertListEqual(sorted(random_list), random_list)
