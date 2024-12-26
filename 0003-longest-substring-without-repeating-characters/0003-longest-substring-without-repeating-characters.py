class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = 0
        start = 0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                start = seen[s[i]] + 1
            seen[s[i]] = i
            curr_len = i - start + 1
            # print(s[i],seen, curr_len)

            max_len = max(max_len, curr_len)
        return max_len