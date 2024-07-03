"""
Title: Find All Anagrams in a String
Problem:

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example:

python

Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Input: s = "abab", p = "ab"
Output: [0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""
from collections import Counter

def find_anagrams(s, p):
    p_count = Counter(p)
    s_count = Counter()
    result = []
    
    p_len = len(p)
    for i in range(len(s)):
        # Add the current character to the window
        s_count[s[i]] += 1
        
        # Remove the character that is left out of the window
        if i >= p_len:
            if s_count[s[i - p_len]] == 1:
                del s_count[s[i - p_len]]
            else:
                s_count[s[i - p_len]] -= 1
        
        # Compare the counts of the window with the counts of p
        if s_count == p_count:
            result.append(i - p_len + 1)
    
    return result

# Test cases
print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
print(find_anagrams("abab", "ab"))         # Output: [0, 1, 2]
print(find_anagrams("af", "be"))           # Output: []
print(find_anagrams("acdcaeccde", "c"))    # Output: [2, 4, 6, 7]
