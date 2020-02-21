from unittest import TestCase 

from util.tester import TestSort
from mergesort.topdown import mergesort

class TestTopDownMergeSort(TestCase, TestSort):
    
    def sort(self, arr: list) -> list:
        return mergesort(arr)