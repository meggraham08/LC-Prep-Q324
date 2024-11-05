class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        for i in range(len(s)):
            if s[i] not in unique:
                unique[s[i]] = 0
            unique[s[i]] += 1
        for i, val_i in enumerate(s):
            if unique[val_i] == 1:
                return i
        return -1