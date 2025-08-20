package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	for i := 0; i < n; i++ {
		rem := make(map[int]int)
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			needed := a[i] - a[j]
			if idx, found := rem[needed]; found {
				fmt.Printf("%d %d %d\n", i+1, j+1, idx+1)
				return
			}
			rem[a[j]] = j
		}
	}
	fmt.Println(-1)

}
