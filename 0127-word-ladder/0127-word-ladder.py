from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)  # To check word existence in O(1)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])  # Store (word, steps)
        visited = set([beginWord])       # To keep track of visited words

        while queue:
            current_word, steps = queue.popleft()

            # Try changing each letter in the current word
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + char + current_word[i + 1:]
                    
                    if next_word == endWord:
                        return steps + 1
                    
                    if next_word in word_set and next_word not in visited:
                        queue.append((next_word, steps + 1))
                        visited.add(next_word)

        return 0  # If endWord is not reachable
