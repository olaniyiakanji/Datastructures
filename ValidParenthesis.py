"""
Title: Valid Parentheses
Problem:

Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example:

python

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: "{[]}"
Output: true
"""
def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

# Test cases
print(is_valid("()"))        # Output: True
print(is_valid("()[]{}"))    # Output: True
print(is_valid("(]"))        # Output: False
print(is_valid("([)]"))      # Output: False
print(is_valid("{[]}"))      # Output: True
print(is_valid("["))         # Output: False
print(is_valid("]"))         # Output: False
