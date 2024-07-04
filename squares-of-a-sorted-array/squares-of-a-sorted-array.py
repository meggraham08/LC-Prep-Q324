class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        right = n -1
        left = 0
        for i in range(n-1, -1 ,-1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -=1
            else:
                square = nums[left]
                left += 1
            res[i] = square * square
        return res
            
        