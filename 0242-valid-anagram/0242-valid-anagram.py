class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frequency counting
        return self.checkFreq(s) == self.checkFreq(t)

        return 
    def checkFreq(self, s):
        my_map = {}
        for i in s:
            my_map[i] = my_map.get(i, 0) + 1
        return my_map