package main

import "fmt"

// GenPascalTriangle generates a pascal's triagle of given depth.
// Returns a two dimensional array
func GenPascalTriangle(depth int) [][]int {
	var triangle [][]int

	firstRow := []int{1}
	triangle = append(triangle, firstRow)

	for i := 1; i < depth; i++ {
		prevRow := triangle[i-1]
		nextRow := []int{1}
		for j := 1; j < i; j++ {
			nextRow = append(nextRow, prevRow[j]+prevRow[j-1])
		}
		nextRow = append(nextRow, 1)
		triangle = append(triangle, nextRow)
	}
	return triangle
}

func main() {
	fmt.Println(GenPascalTriangle(8))
}
