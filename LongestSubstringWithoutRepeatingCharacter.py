"""
Title: Longest Substring Without Repeating Characters
Problem:

Given a string s, find the length of the longest substring without repeating characters.
Example:

python

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

"""
class LongestSubstringFinder:
    def length_of_longest_substring(self, s: str) -> int:
        char_index_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length

# Test cases
finder = LongestSubstringFinder()
print(finder.length_of_longest_substring("abcabcbb"))  # Output: 3
print(finder.length_of_longest_substring("bbbbb"))     # Output: 1
print(finder.length_of_longest_substring("pwwkew"))    # Output: 3
print(finder.length_of_longest_substring(""))          # Output: 0
print(finder.length_of_longest_substring("dvdf"))      # Output: 3
