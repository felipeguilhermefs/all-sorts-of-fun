package asof

// SedgewickQuickSort quicksort inplace (Sedgewick pivot strategy)
func SedgewickQuickSort(arr []int) []int {
	sedgewickQuickSort(arr, 0, len(arr)-1)

	return arr
}

func sedgewickQuickSort(arr []int, low, high int) {
	if high-low < 1 {
		return
	}

	pivotIndex := sedgewickPartition(arr, low, high)

	sedgewickQuickSort(arr, low, pivotIndex)
	sedgewickQuickSort(arr, pivotIndex+1, high)
}

func sedgewickPartition(arr []int, low, high int) int {
	// In Sedgewick we choose the median between low, high and mid elements
	mid := low + (high-low)/2
	if arr[mid] < arr[low] {
		arr[mid], arr[low] = arr[low], arr[mid]
	}
	if arr[high] < arr[low] {
		arr[high], arr[low] = arr[low], arr[high]
	}
	if arr[mid] < arr[high] {
		arr[high], arr[mid] = arr[mid], arr[high]
	}

	pivotIndex := high
	pivot := arr[pivotIndex]
	i := low

	for j := low; j < high; j++ {
		if arr[j] < pivot {
			arr[j], arr[i] = arr[i], arr[j]
			i++
		}
	}

	arr[pivotIndex], arr[i] = arr[i], arr[pivotIndex]

	return i
}
