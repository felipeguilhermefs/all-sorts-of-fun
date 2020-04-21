package asof

// HoareQuickSort quicksort inplace (Hoare pivot strategy)
func HoareQuickSort(arr []int) []int {
	hoareQuickSort(arr, 0, len(arr)-1)

	return arr
}

func hoareQuickSort(arr []int, low, high int) {
	if high-low < 1 {
		return
	}

	pivotIndex := hoarePartition(arr, low, high)

	hoareQuickSort(arr, low, pivotIndex)
	hoareQuickSort(arr, pivotIndex+1, high)
}

func hoarePartition(arr []int, low, high int) int {
	// In Hoare strategy the middle element of the segment is chosen
	pivotIndex := (high + low) / 2
	pivot := arr[pivotIndex]

	i := low - 1
	j := high + 1
	for {
		for {
			i++
			if arr[i] >= pivot {
				break
			}
		}

		for {
			j--
			if arr[j] <= pivot {
				break
			}
		}

		if i >= j {
			return j
		}

		arr[j], arr[i] = arr[i], arr[j]
	}
}
