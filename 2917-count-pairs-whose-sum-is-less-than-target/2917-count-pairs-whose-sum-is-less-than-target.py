class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()  # Step 1: Sort the array
        left = 0
        right = len(nums) - 1
        answer = 0 

        while left < right:
            # Step 2: Calculate the sum of the elements at the pointers
            sum = nums[left] + nums[right]
            print(f"Checking pair ({nums[left]}, {nums[right]}) with sum {sum}")
            
            # Step 3: Check if the sum is less than the target
            if sum < target:
                # All pairs (left, left+1), (left, left+2), ..., (left, right) are valid
                answer += (right - left)
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left

        return answer

        