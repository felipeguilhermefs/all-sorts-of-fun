package asof

import (
	"testing"
)

func TestSedgewickQuickSort(t *testing.T) {
	TestInt(t, SedgewickQuickSort)
}

func BenchmarkSedgewickQuickSort(b *testing.B) {
	BenchmarkInt(b, SedgewickQuickSort)
}
