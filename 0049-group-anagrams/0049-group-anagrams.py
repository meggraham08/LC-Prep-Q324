class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount of list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1
                print(ord(c) - ord("a"))
            res[tuple(count)].append(s)
        return res.values()