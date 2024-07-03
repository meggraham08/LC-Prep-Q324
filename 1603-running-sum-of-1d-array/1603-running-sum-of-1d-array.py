class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        res.append(nums[0])
        for i in range(1, len(nums)):
            res.append(res[i-1]+nums[i])
            i+=1
        return res