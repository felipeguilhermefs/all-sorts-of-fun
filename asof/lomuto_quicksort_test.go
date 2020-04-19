package asof

import (
	"testing"
)

func TestLomutoQuickSort(t *testing.T) {
	TestInt(t, LomutoQuickSort)
}

func BenchmarkLomutoQuickSort(b *testing.B) {
	BenchmarkInt(b, LomutoQuickSort)
}
