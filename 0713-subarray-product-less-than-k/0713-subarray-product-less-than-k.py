class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        prod = 1  # Initialize the product as 1
        i = 0  # Left pointer (start of the sliding window)

        for j in range(len(nums)):  # j is the right pointer
            prod *= nums[j]  # Multiply the current element to the product

            # Shrink the window from the left if the product is >= k
            while prod >= k and i <= j:
                prod //= nums[i]  # Remove nums[i] from the product by dividing
                i += 1  # Move the left pointer (shrink the window)

            # After adjusting the window, all subarrays ending at j are valid
            count += (j - i + 1)
        
        return count