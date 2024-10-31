class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        #brute force
        # {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}
        #  create hash map
        # loop through to find the value one, immediately return the index
        # since you are looping through s!
        for i in range(len(s)):
            if s[i] in unique:
                unique[s[i]] += 1
            else:
                unique[s[i]] = 1
        # loop through string, check if the value of 
        for i, val_i in enumerate(s):
            if unique[val_i] == 1:
                return i
        return -1
  