import unittest

from random import randint
from mergesort.bottomup import mergesort

class TestBottomUpMergeSort(unittest.TestCase):

    def test_should_sort_empty(self):
        empty_list = []
        
        mergesort(empty_list)
        
        self.assertListEqual([], empty_list)

    def test_should_sort_single_element_list(self):
        single_list = [ 42 ]
        
        mergesort(single_list)
        
        self.assertListEqual([ 42 ], single_list)
    
    def test_should_sort_already_sorted_list(self):
        sorted_list = [ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7 ]
        
        mergesort(sorted_list)
        
        self.assertListEqual([ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7 ], sorted_list)

    def test_should_sort_reverse_sorted_list(self):
        reverse_list = [ 7, 6, 5, 4, 3, 2, 1, 0, -1, -2 ]
        
        mergesort(reverse_list)
        
        self.assertListEqual([ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7 ], reverse_list)
    
    def test_should_sort_not_sorted_list(self):
        not_sorted_list = [ 1, -1, 6, 2, 4, 3, 5, 0, 7, -2 ]
        
        mergesort(not_sorted_list)
        
        self.assertListEqual([ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7 ], not_sorted_list)

    def test_should_sort_random_list(self):
        random_size = randint(50, 100) 
        random_list = [ randint(-100, 100) for i in range(random_size) ]
        
        sorted_list = sorted(random_list)

        mergesort(random_list)
        
        self.assertListEqual(sorted_list, random_list)
