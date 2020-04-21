package asof

import (
	helper "asof/helper"
	"testing"
)

func TestTopDownMergeSort(t *testing.T) {
	helper.TestInt(t, TopDownMergeSort)
}

func BenchmarkTopDownMergeSort(b *testing.B) {
	helper.BenchmarkInt(b, TopDownMergeSort)
}
