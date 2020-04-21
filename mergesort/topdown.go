package asof

// TopDownMergeSort a classical implementation
// original array is not modified
func TopDownMergeSort(arr []int) []int {
	length := len(arr)
	if length < 2 {
		return arr
	}

	mid := length / 2
	left := TopDownMergeSort(arr[:mid])
	right := TopDownMergeSort(arr[mid:])

	return merge(left, right)
}

func merge(left, right []int) []int {
	li := 0
	ri := 0

	maxLeft := len(left)
	maxRight := len(right)

	merged := []int{}

	for i := 0; i < (maxLeft + maxRight); i++ {
		if li < maxLeft && (ri >= maxRight || left[li] <= right[ri]) {
			merged = append(merged, left[li])
			li++
		} else {
			merged = append(merged, right[ri])
			ri++
		}
	}

	return merged
}
