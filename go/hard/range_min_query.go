// description: RMQSQ - Range Minimum Query
// difficulty: Hard
// leetcode_num:
// leetcode_url: https://www.spoj.com/problems/RMQSQ/
// You are given a list of N numbers and Q queries. Each query is specified
// by two numbers i and j; the answer to each query is the minimum number
// between the range [i, j] (inclusive).

package main

import "fmt"

const (
	MAX_N = 100000
	LOG   = 17
)

var m [MAX_N][LOG]int
var log [MAX_N]int

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func query(nums []int, l, r int) int {
	ln := r - l + 1
	k := log[ln]
	return min(m[l][k], m[r-(1<<k)+1][k])
}

func main() {
	// Sample input
	nums := []int{2, 3, 7, 1, 8, 6, 9, 4, 5}
	n := len(nums)

	// Build the log table
	log[1] = 0
	for i := 2; i <= n; i++ {
		log[i] = log[i/2] + 1
	}

	// Base values for the sparse table. We'll use
	// dynamic programming to build the table in next step.
	for i := 0; i < n; i++ {
		m[i][0] = nums[i]
	}

	// Build the sparse table to make faster queries of O(1)
	// Building this sparse table takes O(n * log n) time
	for k := 1; k < LOG; k++ {
		for i := 0; i+(1<<k)-1 < n; i++ {
			m[i][k] = min(m[i][k-1], m[i+(1<<(k-1))][k-1])
		}
	}

	// Call multiple queries. This only takes O(1) time
	fmt.Println(query(nums, 4, 6))
	fmt.Println(query(nums, 2, 6))
}
