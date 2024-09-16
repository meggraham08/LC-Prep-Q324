class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # okay so you could make a hashmap with a count, yeah?
        if len(s) == 1: return True
        s_map = {}
        for i in s:
            s_map[i] = s_map.get(i , 0) + 1
        # now i want to confirm that i have an even number of all but 1 char.
        # can do this by looping through the values and making sure they are an even values and then at most one odd value
        # store in a list and then check that the list has those values and then 1 single value
        evenCount = 0
        oddCount = 0
        if len(s_map.values()) == 1:
            return True
        for value in s_map.values():
            if value % 2 == 0:
                evenCount+= 1
            elif value % 2 == 1:
                oddCount += 1
        print(evenCount, oddCount)

        # if len(s) == 2 and s[0] == s[1]:
        #     return True

        if oddCount <= 1:
            return True
        else:
            return False
