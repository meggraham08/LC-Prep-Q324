class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""
        
        def checkPal(l, r):
            nonlocal resLen, res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > resLen:
                    res = s[l:r + 1]
                    resLen = currLen
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # Check for odd-length palindromes
            checkPal(i, i)
            # Check for even-length palindromes
            checkPal(i, i + 1)
        
        return res
