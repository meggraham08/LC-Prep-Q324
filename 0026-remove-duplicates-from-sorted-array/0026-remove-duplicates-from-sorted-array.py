class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ref = nums[0]

        i = 1
        while i < len(nums):
            if ref == nums[i]:
                nums.pop(i)
            else:
                ref = nums[i]
                i += 1
        
        return len(nums)