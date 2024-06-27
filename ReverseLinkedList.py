"""
roblem:

Given the head of a singly linked list, reverse the list, and return the reversed list.
Example:

python

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Helper function to convert list to ListNode
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert ListNode to list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
head1 = list_to_linkedlist([1, 2, 3, 4, 5])
reversed_head1 = reverse_list(head1)
print(linkedlist_to_list(reversed_head1))  # Output: [5, 4, 3, 2, 1]

head2 = list_to_linkedlist([1, 2])
reversed_head2 = reverse_list(head2)
print(linkedlist_to_list(reversed_head2))  # Output: [2, 1]

head3 = list_to_linkedlist([])
reversed_head3 = reverse_list(head3)
print(linkedlist_to_list(reversed_head3))  # Output: []
