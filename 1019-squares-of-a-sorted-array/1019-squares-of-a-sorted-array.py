class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        n = len(nums)
        right = n -1
        res = [0] * n
        #range are (start, stop, step)
        for i in range(n-1 , -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left +=1
            res[i] = square * square
        return res


    # [-4,-1,0,3,10]

            
        