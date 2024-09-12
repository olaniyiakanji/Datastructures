"""
Title: Word Ladder
Problem:

Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

Return 0 if no such transformation sequence exists.
Example:

python

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: The shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog".

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, so no transformation is possible.

"""
from collections import deque

def word_ladder(beginWord, endWord, wordList):
    word_set = set(wordList)  # Convert wordList to a set for fast lookup
    if endWord not in word_set:
        return 0
    
    queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)
    
    while queue:
        current_word, steps = queue.popleft()
        
        # Try changing every letter in the current word
        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = current_word[:i] + char + current_word[i+1:]
                
                # If we find the endWord, return the number of steps
                if new_word == endWord:
                    return steps + 1
                
                # If the new word is in the word list, add it to the queue
                if new_word in word_set:
                    queue.append((new_word, steps + 1))
                    word_set.remove(new_word)  # Mark it as visited
    
    return 0  # No valid transformation sequence

# Test cases
print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Output: 5
print(word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]))        # Output: 0
