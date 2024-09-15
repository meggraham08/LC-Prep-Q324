class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pCount = {}
        sCount = {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        # for i in range(len(p)):
        #     if i not in pCount:
        #         pCount[p[i]] = 1
        #     else:
        #         pCount[p[i]] += 1
        #     if i not in sCount:
        #         sCount[s[i]] = 1
        #     else:
        #         sCount[s[i]] += 1
            # sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        left = 0
        for right in range(len(p), len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            sCount[s[left]] -= 1
            if sCount[s[left]] == 0:
                sCount.pop(s[left])
            left += 1
            if sCount == pCount:
                res.append(left)

        return res



        # left = 0
        # right = len(p) - 1
        # res = []
        # for i in p:
        #     if i not in pCount:
        #         pCount[i] = 1
        #     else:
        #         pCount[i] += 1
        # while left < right:
        #     if left not in sCount:
        #         sCount[s[left]] = 1
        #     else:
        #         sCount[s[left]] +=1
        #     if sCount == pCount:
        #         res.append(left)
        #     left += 1
        #     right += 1
        # print(pCount, sCount)
        # return left
            