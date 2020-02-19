# Mergesort Top-Down implementation
def mergesort(arr):
    __mergesort(arr, 0, len(arr))

def __mergesort(arr, start, end):
    # if it is only one (or empty), it is already sorted
    if end - start < 2:
        return
    
    middle = (end + start) // 2
    
    __mergesort(arr, start, middle)
    __mergesort(arr, middle, end)
    
    __merge(arr, start, middle, end)

def __merge(arr, begin, middle, end):
    # indexes to keep track of each half
    li = 0
    ri = 0

    # halves to merge
    left = arr[begin:middle]
    right = arr[middle:end]

    max_left = len(left)
    max_right = len(right)

    # Each iteration will choose the halves min element
    # its easy since they are already sorted o.o
    for i in range(begin, end):
        if li < max_left and (ri >= max_right or left[li] <= right[ri]):
            arr[i] = left[li]
            li += 1
        else:
            arr[i] = right[ri]
            ri += 1