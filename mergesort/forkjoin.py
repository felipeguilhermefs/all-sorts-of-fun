""" Fork-Join Mergesort

!!Important!! it is a implementation to present the algorithm,
if you need to sort a list use list.sort for in place, or sorted
for a new list.
"""

import math
import multiprocessing as mp

from random import randint
from unittest import TestCase

# We will use mergesort topdown, but could be any version
from mergesort.topdown import mergesort as ms
from mergesort.topdown import merge


def mergesort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    cpu_count = mp.cpu_count()

    # We take a slice for each cpu
    slice_length = math.ceil(len(arr) / cpu_count)
    slices = (arr[i: i+slice_length] for i in range(0, len(arr), slice_length))

    with mp.Pool(processes=cpu_count) as pool:
        # The slices sorting is distributed
        sorted_slices = pool.map(ms, slices)

        # We merge iteratively each pair of slices
        while len(sorted_slices) > 1:

            # We ensure that each slice has a pair
            if len(sorted_slices) % 2 != 0:
                sorted_slices.append([])

            pairs_to_merge = (
                (sorted_slices[i], sorted_slices[i + 1])
                for i in range(0, len(sorted_slices), 2))

            sorted_slices = pool.starmap(merge, pairs_to_merge)

        return sorted_slices[0]

##################
### Some Tests ###
##################


class TestForkJoinMergeSort(TestCase):

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
            [-1, 0, 1, 2, 3, 4, 5, 6, 7],
            mergesort([1, -1, 6, 2, 4, 3, 5, 0, 7]))

    def test_should_sort_random_list(self):
        random_size = randint(50, 100)
        random_list = [randint(-100, 100) for i in range(random_size)]

        self.assertListEqual(sorted(random_list),
                             mergesort(random_list))
