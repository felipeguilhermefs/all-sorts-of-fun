package asof

import (
	helper "asof/helper"
	"testing"
)

func TestHoareQuickSort(t *testing.T) {
	helper.TestInt(t, HoareQuickSort)
}

func BenchmarkHoareQuickSort(b *testing.B) {
	helper.BenchmarkInt(b, HoareQuickSort)
}
