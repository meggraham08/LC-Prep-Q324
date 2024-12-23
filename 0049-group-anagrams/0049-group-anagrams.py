class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        for s in strs:
            answer[tuple(sorted(s))].append(s)
        print(answer)
        return list(answer.values())
