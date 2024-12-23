class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1

        for index, i in enumerate(s):
            print(index, i, freq[i])
            if freq[i] == 1:
                return index
        return -1