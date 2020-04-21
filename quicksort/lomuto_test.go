package asof

import (
	helper "asof/helper"
	"testing"
)

func TestLomutoQuickSort(t *testing.T) {
	helper.TestInt(t, LomutoQuickSort)
}

func BenchmarkLomutoQuickSort(b *testing.B) {
	helper.BenchmarkInt(b, LomutoQuickSort)
}
