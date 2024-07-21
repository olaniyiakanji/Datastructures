"""
Title: Reverse Linked List
Problem:

Given the head of a singly linked list, reverse the list, and return the reversed list.
Example:

python

Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Input: head = [1, 2]
Output: [2, 1]

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

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    print(vals)

# Test cases
head1 = create_linked_list([1, 2, 3, 4, 5])
reversed_list1 = reverse_list(head1)
print_linked_list(reversed_list1)  # Output: [5, 4, 3, 2, 1]

head2 = create_linked_list([1, 2])
reversed_list2 = reverse_list(head2)
print_linked_list(reversed_list2)  # Output: [2, 1]

head3 = create_linked_list([])
reversed_list3 = reverse_list(head3)
print_linked_list(reversed_list3)  # Output: []
