from unittest import TestCase 

from util.tester import TestSort
from mergesort.bottomup import mergesort

class TestBottomUpMergeSort(TestCase, TestSort):
    
    def sort(self, arr: list) -> list:
        return mergesort(arr)