package main

import "fmt"

// FindNumberOfIslands finds the number of islands given a two dimensional
// grid where 1s represent land area and 0s represent water.
func FindNumberOfIslands(grid [][]byte) int {
	numIslands := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[i]); j++ {
			if grid[i][j] == '1' {
				numIslands++
				expandIsland(grid, i, j)
			}
		}
	}
	return numIslands
}

// Recursive DFS for finding island boundaries and making them a single unit.
// Ie. mark it as 0
func expandIsland(grid [][]byte, i, j int) {
	if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[i]) || grid[i][j] == '0' {
		return
	}
	grid[i][j] = '0'
	expandIsland(grid, i-1, j) // top expansion
	expandIsland(grid, i+1, j) // bottom expansion
	expandIsland(grid, i, j-1) // left expansion
	expandIsland(grid, i, j+1) // right expansion
}

func main() {
	grid := [][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '0', '0', '0'},
	}

	fmt.Println(FindNumberOfIslands(grid))
}
