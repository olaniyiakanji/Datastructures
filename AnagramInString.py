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
Explanation: The substring "cba" from index 0 and "bac" from index 6 are anagrams of "abc".

Input: s = "abab", p = "ab"
Output: [0, 1, 2]
Explanation: The substring "ab" from index 0, "ba" from index 1, and "ab" from index 2 are anagrams of "from collections import Counter
"""
def find_anagrams(s, p):
    p_count = Counter(p)
    s_count = Counter()
    
    result = []
    p_length = len(p)
    
    for i in range(len(s)):
        s_count[s[i]] += 1
        
        if i >= p_length:
            if s_count[s[i - p_length]] == 1:
                del s_count[s[i - p_length]]
            else:
                s_count[s[i - p_length]] -= 1
        
        if s_count == p_count:
            result.append(i - p_length + 1)
    
    return result

# Test cases
print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
print(find_anagrams("abab", "ab"))         # Output: [0, 1, 2]
print(find_anagrams("af", "be"))           # Output: []
print(find_anagrams("aa", "bb"))           # Output: []
print(find_anagrams("baa", "aa"))          # Output: [1]




