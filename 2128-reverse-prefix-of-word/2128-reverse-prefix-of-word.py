class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        final = ""
        for c in range(len(word)):
            if word[c] == ch:
                index = c
                break
        for i in range(index,-1,-1):
            print(word[i])
            final += word[i]
        
        return final + word[index+1:]