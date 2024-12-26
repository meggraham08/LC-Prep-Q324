class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # similar to your previous solution - track counts
        seen = {}
        max_len = 0
        start = 0
        max_freq = 0  # track most frequent char count
        
        for i in range(len(s)):
            # add current char to seen (count frequencies)
            seen[s[i]] = seen.get(s[i], 0) + 1
            
            # track highest frequency in current window
            max_freq = max(max_freq, seen[s[i]])
            
            # current window length
            curr_window = i - start + 1
            
            # if chars to replace > k, shrink window
            if curr_window - max_freq > k:
                # remove start char from counts
                seen[s[start]] -= 1
                start += 1
            
            # update max_len (window size is i - start + 1)
            max_len = max(max_len, i - start + 1)
            
        return max_len