from random import randint

class TestSort:

    sort = None
    def sort(self, arr: list) -> list:
        return []

    def test_should_sort_empty(self):
        empty_list = self.sort([])
        
        self.assertListEqual([], empty_list)

    def test_should_sort_single_element_list(self):
        single_list = self.sort([ 42 ])
        
        self.assertListEqual([ 42 ], single_list)
    
    def test_should_sort_already_sorted_list(self):
        sorted_list = self.sort([ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7 ])
        
        self.assertListEqual([ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7 ], sorted_list)

    def test_should_sort_reverse_sorted_list(self):
        reverse_list = self.sort([ 7, 6, 5, 4, 3, 2, 1, 0, -1, -2 ])
        
        self.assertListEqual([ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7 ], reverse_list)
    
    def test_should_sort_not_sorted_list(self):
        not_sorted_list = self.sort([ 1, -1, 6, 2, 4, 3, 5, 0, 7, -2 ])
        
        self.assertListEqual([ -2, -1, 0, 1, 2, 3, 4, 5, 6, 7 ], not_sorted_list)

    def test_should_sort_random_list(self):
        random_size = randint(50, 100) 
        random_list = [ randint(-100, 100) for i in range(random_size) ]
        
        self.assertListEqual(sorted(random_list), self.sort(random_list))

    def test_should_sort_big_list(self):
        big_list = [ randint(-10000, 10000) for i in range(100000) ]
        
        self.assertListEqual(sorted(big_list), self.sort(big_list))