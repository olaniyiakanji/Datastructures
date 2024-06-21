"""
Title: Implement a Stack Using Queues
Problem:

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support the following operations: push(x) (adding an element to the stack), pop() (removing the top element of the stack), top() (getting the top element of the stack), and empty() (checking whether the stack is empty).

You can assume that all operations are valid (e.g., pop or top operations will not be called on an empty stack).
Example:


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False

"""
from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Push element to q2
        self.q2.append(x)
        # Push all the elements of q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # Remove the element from the front of q1
        return self.q1.popleft()

    def top(self) -> int:
        # Get the front element of q1
        return self.q1[0]

    def empty(self) -> bool:
        # Check if q1 is empty
        return not bool(self.q1)

# Test cases
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False
