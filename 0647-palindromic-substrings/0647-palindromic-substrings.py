class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        # Iterate through all possible palindrome centers
        for center in range(2 * len(s) - 1):
            left = center // 2
            right = left + center % 2
            
            # Expand around the center to find palindromic substrings
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count