# Mergesort Bottom-Up implementation
def mergesort(arr):
    if len(arr) < 2:
        return

    size = len(arr)
    
    width = 1
    while width < size:

        for offset in range(0, size, width * 2):
            __merge(arr, offset, min(offset + width, size), min(offset + 2 * width, size))
        
        width *= 2

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
