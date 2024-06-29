class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            new = abs(nums[i]) - 1
            if nums[new] > 0:
                nums[new] *= -1
            

        for i in range(1,len(nums)+1):
            if nums[i-1] > 0:
                res.append(i)
        return res
        