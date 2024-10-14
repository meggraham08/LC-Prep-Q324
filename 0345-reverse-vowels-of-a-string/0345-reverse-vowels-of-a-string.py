class Solution:
    def reverseVowels(self, s: str) -> str:
        # IceCreAm
        # initial thought is to break make it lowercase
        # icecream
        # create a list of vowels
        # icecream
        # 2 pointer, one on very left one on very right
        # look for 2 vowels, once two are found, swap places and increment
        # if c in vowels 
        left = 0
        right = len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I' ,'O', 'U']
        s = list(s)
        while left < right:
            print(s[left], s[right])
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                print(s[left], s[right])
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
        print(s)
        return "".join(s) 