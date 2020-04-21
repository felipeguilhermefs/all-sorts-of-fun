package asof

// BottomUpMergeSort mergesort 'almost' inplace
func BottomUpMergeSort(arr []int) []int {
	length := len(arr)
	if length < 2 {
		return arr
	}

	width := 1
	for width < length {
		for offset := 0; offset < length; offset += width * 2 {
			mid := min(offset+width, length)
			end := min(offset+2*width, length)
			mergeInplace(arr, offset, mid, end)
		}

		width *= 2
	}

	return arr
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}

func mergeInplace(arr []int, begin, middle, end int) {
	li := 0
	ri := 0

	left := make([]int, middle-begin)
	copy(left, arr[begin:middle])

	right := make([]int, end-middle)
	copy(right, arr[middle:end])

	maxLeft := len(left)
	maxRight := len(right)

	for i := begin; i < end; i++ {
		if li < maxLeft && (ri >= maxRight || left[li] <= right[ri]) {
			arr[i] = left[li]
			li++
		} else {
			arr[i] = right[ri]
			ri++
		}
	}
}
