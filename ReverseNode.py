"""
Title: Reverse Nodes in k-Group
Problem:

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
Example:

python

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_linked_list(head, k):
        new_head, ptr = None, head
        while k:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head
    
    count = 0
    ptr = head
    
    while count < k and ptr:
        ptr = ptr.next
        count += 1
    
    if count == k:
        reversed_head = reverse_linked_list(head, k)
        head.next = reverse_k_group(ptr, k)
        return reversed_head
    
    return head

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
list1 = create_linked_list([1, 2, 3, 4, 5])
k1 = 2
result1 = reverse_k_group(list1, k1)
print_linked_list(result1)  # Output: [2, 1, 4, 3, 5]

list2 = create_linked_list([1, 2, 3, 4, 5])
k2 = 3
result2 = reverse_k_group(list2, k2)
print_linked_list(result2)  # Output: [3, 2, 1, 4, 5]
