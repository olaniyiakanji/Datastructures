"""
Title: Linked List Cycle
Problem:

Given the head of a linked list, determine if the linked list has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where the tail connects to. If pos is -1, then there is no cycle in the linked list.

Example:

python
Copy code
Input: head = [3,2,0,-4], pos = 1
Output: True
Explanation: There is a cycle in the linked list, where the tail connects to the second node.

Input: head = [1,2], pos = 0
Output: True
Explanation: There is a cycle in the linked list, where the tail connects to the first node.

Input: head = [1], pos = -1
Output: False
Explanation: There is no cycle in the linked class ListNode:
 """
    
def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    if not head:
        return False

    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
        
    return True

# Helper function to create a linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    cycle_node = None if pos == -1 else head
    
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current
    
    if pos != -1:
        current.next = cycle_node
    
    return head

# Test cases
head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
print(has_cycle(head1))  # Output: True

head2 = create_linked_list_with_cycle([1, 2], 0)
print(has_cycle(head2))  # Output: True

head3 = create_linked_list_with_cycle([1], -1)
print(has_cycle(head3))  # Output: False

head4 = create_linked_list_with_cycle([1, 2, 3, 4, 5], 2)
print(has_cycle(head4))  # Output: True

head5 = create_linked_list_with_cycle([], -1)
print(has_cycle(head5))  # Output: False


