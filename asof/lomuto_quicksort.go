package asof

// LomutoQuickSort quicksort inplace
func LomutoQuickSort(arr []int) []int {
	lomutoQuickSort(arr, 0, len(arr)-1)
	return arr
}

func lomutoQuickSort(arr []int, low, high int) {
	if high-low < 1 {
		return
	}

	pivotIndex := lomutoPartition(arr, low, high)

	lomutoQuickSort(arr, low, pivotIndex-1)
	lomutoQuickSort(arr, pivotIndex, high)
}

func lomutoPartition(arr []int, low, high int) int {
	// In Lomuto strategy the last element of the segment is chosen
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
