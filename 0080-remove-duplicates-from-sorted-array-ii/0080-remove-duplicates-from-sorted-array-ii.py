class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        
        for i in range(1,len(nums)):
            if nums[i] != nums[count - 1] or (count == 1 or nums[i] != nums[count - 2]):
                nums[count] = nums[i]
   
                count+= 1
        return count

        