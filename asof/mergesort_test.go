package asof

import (
	"testing"
)

func TestMergeSort(t *testing.T) {
	TestInt(t, MergeSort)
}

func BenchmarkMergeSort(b *testing.B) {
	BenchmarkInt(b, MergeSort)
}
