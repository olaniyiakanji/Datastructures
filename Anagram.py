"""
Title: Find All Anagrams in a String
Problem:
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
python
Copy code
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation:
The substring starting at index 0 is "cba", which is an anagram of "abc".
The substring starting at index 6 is "bac", which is an anagram of "abc".

Input: s = "abab", p = "ab"
Output: [0, 1, 2]
Explanation:
The substring starting at index 0 is "ab", which is an anagram of "ab".
The substring starting at index 1 is "ba", which is an anagram of "ab".
The substring starting at index 2 is "ab", which is an anagram of "ab".
"""
from collections import Counter

def find_anagrams(s, p):
    p_count = Counter(p)
    s_count = Counter()
    result = []
    
    for i in range(len(s)):
        s_count[s[i]] += 1
        
        # Remove the leftmost character from the window if its size exceeds the length of p
        if i >= len(p):
            if s_count[s[i - len(p)]] == 1:
                del s_count[s[i - len(p)]]
            else:
                s_count[s[i - len(p)]] -= 1
        
        # If the counts match, we found an anagram
        if s_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

# Test cases
print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
print(find_anagrams("abab", "ab"))         # Output: [0, 1, 2]
print(find_anagrams("af", "be"))           # Output: []
print(find_anagrams("abc", "cba"))         # Output: [0]
print(find_anagrams("abacbabc", "abc"))    # Output: [1, 2, 3, 5]
