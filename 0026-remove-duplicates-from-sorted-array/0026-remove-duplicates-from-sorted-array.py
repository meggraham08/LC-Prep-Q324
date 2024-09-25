class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Start count at 1 because the first element is always unique
        count = 1
        n = len(nums)

        # Loop through the array starting from the second element
        for i in range(1, n):
            if nums[i] != nums[i - 1]:  # Compare current element with the previous one
                nums[count] = nums[i]  # Place unique element at `count`
                count += 1

        return count
        # nums.sort() # O(N)
        # left = 0
        # right = len(nums)-1
        # while left < right:
        #     if nums[left] == nums[right]:
        #         nums.pop(left)
        #         left += 1
        #     else:
        #         right -= 1
        