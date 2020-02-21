from unittest import TestCase
from random import randint


# Mergesort Top-Down implementation
def mergesort(arr):
    return __mergesort(arr, 0, len(arr))


def __mergesort(arr, start, end):
    # if it is only one (or empty), it is already sorted
    if end - start < 2:
        return arr

    middle = (end + start) // 2

    __mergesort(arr, start, middle)
    __mergesort(arr, middle, end)

    __merge(arr, start, middle, end)

    return arr


def __merge(arr: list, begin: int, middle: int, end: int):
    # indexes to keep track of each half
    li = 0
    ri = 0

    # halves to merge
    left = arr[begin:middle]
    right = arr[middle:end]

    max_left = len(left)
    max_right = len(right)

    # Each iteration will choose the halves min element
    # its easy since each half is already sorted o.o
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
