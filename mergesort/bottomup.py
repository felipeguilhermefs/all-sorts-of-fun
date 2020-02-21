""" Mergesort Bottom-Up (iterative)

Time complexity: O(n log n)
Space complextity: O(n)
Stable: Yes

The bottom-up version of a mergesort uses a iterative approach,
where the collection is considered an collection of 'n' subcollections
of size 1.

To execute the sort, each subcollection is merged with the next (this
process is called a run). In each run the subcollections size are doubled,
and they occur iteratively until every subcollection is merged
together.

Ex:

    Collection: [ -1, 4, 3, 0, 5, -2]

    First Run: Width (1)
        - [-1] merge [4] => [-1, 4]
        - [3] merge [0] => [0, 3]
        - [5] merge [-2] => [-2, 5]
        - Collection: [-1, 4, 0, 3, -2, 5]

    Second Run: Width (2)
        - [-1, 4] merge [0, 3] => [-1, 0, 3, 4]
        - [-2, 5] merge [] => [-2, 5]
        - Collection: [-1, 0, 3, 4, -2, 5]

    Third Run: Width (4)
        - [-1, 0, 3, 4] merge [-2, 5] => [-2, -1, 0, 3, 4, 5]
        - Collection: [-2, -1, 0, 3, 4, 5]

In a language like Python, where (until now) there is no tail call
optimization, this iterative approach could prove to be "safer"
than the top-down version.

"""

def mergesort(arr: list) -> list:
    """
    Sort the list using a bottom-up strategy. 
    
    !!Important the list is mutated
    
    Parameters
    ----------
    arr : list
    The array of numbers to be sorted
    
    Returns
    -------
    
    list
    The same list passed as a parameter. Just for facilitate testing
    and saving a line of code in some cases.
    """

    # There is no need to sort if it is empty or has a single element
    if len(arr) < 2:
        return arr

    size = len(arr)
    
    width = 1
    while width < size:

        for start in range(0, size, width * 2):
            middle = min(start + width, size)
            end = min(start + 2 * width, size)
            
            __merge(arr, start, middle, end)
        
        width *= 2
    
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