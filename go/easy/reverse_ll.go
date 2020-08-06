// description: Reverse Linked List
// difficulty: Easy
// leetcode_num: 206
// leetcode_url: https://leetcode.com/problems/reverse-linked-list/

package main

import "fmt"

// Node represents a LL Node
type Node struct {
	data int
	next *Node
}

// ReverseLL reverses the whole list given a head node
func ReverseLL(node *Node) (newHead *Node) {
	if node == nil {
		return nil
	}

	currentNode := node
	var prevNode *Node
	for currentNode != nil {
		nextNode := currentNode.next
		currentNode.next = prevNode
		prevNode = currentNode
		currentNode = nextNode
	}

	newHead = prevNode
	return newHead
}

// PrintLL prints the items in the given LL
func PrintLL(node *Node) {
	for node != nil {
		fmt.Printf("%d ", node.data)
		node = node.next
	}
	fmt.Printf("\n")
}

func main() {
	var prev *Node
	var head *Node
	for i := 0; i < 10; i++ {
		n := new(Node)
		n.data = i
		if head == nil {
			head = n
		}
		n.next = nil
		if prev != nil {
			prev.next = n
		}
		prev = n
	}
	PrintLL(head)
	head = ReverseLL(head)
	PrintLL(head)
}
