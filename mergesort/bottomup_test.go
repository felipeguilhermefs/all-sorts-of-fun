package asof

import (
	helper "asof/helper"
	"testing"
)

func TestBottomUpMergeSort(t *testing.T) {
	helper.TestInt(t, BottomUpMergeSort)
}

func BenchmarkBottomUpMergeSort(b *testing.B) {
	helper.BenchmarkInt(b, BottomUpMergeSort)
}
