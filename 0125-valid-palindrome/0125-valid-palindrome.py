class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]", '', s.lower())
        reversed_s = s[::-1]
        return reversed_s == s