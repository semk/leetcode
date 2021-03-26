// description: Number of Islands
// difficulty: Medium
// leetcode_num: 200
// leetcode_url: https://leetcode.com/problems/number-of-islands/
//
// Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
// An island is surrounded by water and is formed by connecting adjacent lands
// horizontally or vertically. You may assume all four edges of the grid are all
// surrounded by water.
//
// Example 1:
//
// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1
// Example 2:
//
// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3

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
		{'0', '0', '1', '0', '0'},
	}

	fmt.Println(FindNumberOfIslands(grid))
}
