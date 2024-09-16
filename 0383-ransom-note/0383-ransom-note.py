class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # BRUTE FORCE
        # check that only one letter to use in ransom note with the amount of letters from magazine
        # you can have extra magazine letters
        # if there are fewer letters in magazine than there are ransomNote, return false
        if len(magazine) < len(ransomNote): return False
        # if they are same size and not equal, return false
        if len(magazine) == len(ransomNote) and sorted(magazine) != sorted(ransomNote): return False
        rnCount = [0] * 26
        magCount = [0] * 26
        # make a array that houses all the letters and counts there are
        # for both ransomeNote and magazie
        for i in magazine:
            magCount[ord(i) - ord("a")] += 1
        print("magCount" , magCount)
        for i in ransomNote:
            rnCount[ord(i) - ord("a")] += 1
        print("ransomNote",  rnCount)
        # if the elements for each are the same, and the count for mag is equal or greater than 
        # ransomeCount, return True
        for i in range(len(magCount)-1):
            checkVal = magCount[i] - rnCount[i]
            print("checkVal", checkVal)
            if checkVal < 0:
                return False
        return True
        # a b c d e f g h i j k l m n o p q r s t u v w z y z   count
        # 6 3 1 2 3 2 2 2 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0   magazine
        # 0 0 0 0 1 1 0 1 2 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0   ransomeNote
        # 6 3 1 2 2 1 2 2 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0     total 
