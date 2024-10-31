class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        for i in s:
            if i not in unique:
                unique[i] = 0
            unique[i] += 1
        print(unique)
        for i, val in enumerate(s):
            if unique[val] == 1:
                return i
        return -1

