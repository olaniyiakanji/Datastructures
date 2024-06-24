"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the two input lists.
Example:

python

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]

Solution:

We can use a dummy node to simplify the merging process and maintain a pointer to build the new sorted list. By iterating through both lists, we compare the current nodes of both lists and append the smaller one to the new list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # If one of the lists is not empty, append it to the result
    current.next = l1 if l1 else l2

    return dummy.next

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

# Helper function to print ListNode as list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
l1 = list_to_linkedlist([1, 2, 4])
l2 = list_to_linkedlist([1, 3, 4])
merged_list = merge_two_lists(l1, l2)
print(linkedlist_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]

l1 = list_to_linkedlist([])
l2 = list_to_linkedlist([])
merged_list = merge_two_lists(l1, l2)
print(linkedlist_to_list(merged_list))  # Output: []

l1 = list_to_linkedlist([])
l2 = list_to_linkedlist([0])
merged_list = merge_two_lists(l1, l2)
print(linkedlist_to_list(merged_list))  # Output: [0]
