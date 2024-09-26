class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(len(nums)):
            ans = nums[i] * nums[i]
            res.append(ans)
        res.sort()
        return res