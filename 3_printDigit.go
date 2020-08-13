package main

import (
	"fmt"
	"math"
)

func main() {
	var N int = 1345679

	var digit []int
	for N > 0 {
		digit = append(digit, N%10)
		N /= 10
	}

	for len(digit)-1 >= 0 {
		var num float64 = float64(digit[len(digit)-1]) * math.Pow10(len(digit)-1)
		fmt.Printf("%d\n", int(num))
		digit = digit[:len(digit)-1]
	}
}
