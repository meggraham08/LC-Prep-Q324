class Solution:
    def missingNumber(self, nums: List[int]) -> int:

    #Sort the Array - O(nlogn)
    # Find the largest element - O(n)
    # Check the length of the array - O(1)
    # if length of array is equal to the largest - O(1)
    #     Then decrement - O(n)
    # if not length of array is equal to the largest  - O(1)
    #     return largest + 1
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            elif nums[0] == 1:
                return 0
        
        # return nums[0]
        nums.sort()
        largestElement = len(nums) # 3
        largest = max(nums) # 3
        if largestElement == largest:
            # largest -= 1
            for i, val_i in enumerate(nums):
                if nums[len(nums) - i - 1] == largest:
                    largest -= 1
                else:
                    return largest
            return 0
        else:
            return largest + 1

                
        
        # total = sum(nums) - len(nums) / 2
        # return total
        # 