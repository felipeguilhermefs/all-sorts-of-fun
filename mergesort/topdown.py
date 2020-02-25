""" Top-Down Mergesort

!!Important!! it is a implementation to present the algorithm,
if you need to sort a list use list.sort for in place, or sorted
for a new list.
"""

from random import randint
from unittest import TestCase


def mergesort(arr: list) -> list:
    length = len(arr)
    if length < 2:
        return arr

    mid = length // 2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)


def merge(left: list, right: list) -> list:
    li = 0
    ri = 0

    max_left = len(left)
    max_right = len(right)

    merged = []
    for _ in range(max_left + max_right):
        if li < max_left and (ri >= max_right or left[li] <= right[ri]):
            merged.append(left[li])
            li += 1
        else:
            merged.append(right[ri])
            ri += 1

    return merged

##################
### Some Tests ###
##################


class TestTopDownMergeSort(TestCase):

    def test_should_sort_empty(self):
        self.assertListEqual([], mergesort([]))

    def test_should_sort_single_element_list(self):
        self.assertListEqual([42], mergesort([42]))

    def test_should_sort_already_sorted_list(self):
        self.assertListEqual(
            [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7],
            mergesort([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]))

    def test_should_sort_reverse_sorted_list(self):
        self.assertListEqual(
            [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7],
            mergesort([7, 6, 5, 4, 3, 2, 1, 0, -1, -2]))

    def test_should_sort_not_sorted_list(self):
        self.assertListEqual(
            [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7],
            mergesort([1, -1, 6, 2, 4, 3, 5, 0, 7, -2]))

    def test_should_sort_random_list(self):
        random_size = randint(50, 100)
        random_list = [randint(-100, 100) for i in range(random_size)]

        self.assertListEqual(sorted(random_list), mergesort(random_list))
