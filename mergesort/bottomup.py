from mergesort.merge import merge

# Mergesort Bottom-Up implementation
def mergesort(arr):
    if len(arr) < 2:
        return

    size = len(arr)
    
    width = 1
    while width < size:

        for offset in range(0, size, width * 2):
            merge(arr, offset, min(offset + width, size), min(offset + 2 * width, size))
        
        width *= 2
