from mergesort.merge import merge

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
    
    merge(arr, start, middle, end)

