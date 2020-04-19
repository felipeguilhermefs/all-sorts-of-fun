package asof

import (
	"testing"
)

func TestHoareQuickSort(t *testing.T) {
	TestInt(t, HoareQuickSort)
}

func BenchmarkHoareQuickSort(b *testing.B) {
	BenchmarkInt(b, HoareQuickSort)
}
