from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        print(words)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            print(start)
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue
                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)
        return False