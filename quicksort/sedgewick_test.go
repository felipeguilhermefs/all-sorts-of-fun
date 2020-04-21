package asof

import (
	helper "asof/helper"
	"testing"
)

func TestSedgewickQuickSort(t *testing.T) {
	helper.TestInt(t, SedgewickQuickSort)
}

func BenchmarkSedgewickQuickSort(b *testing.B) {
	helper.BenchmarkInt(b, SedgewickQuickSort)
}
