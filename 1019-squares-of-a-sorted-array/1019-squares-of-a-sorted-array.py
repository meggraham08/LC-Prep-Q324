class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l = 0
        r = len(nums)-1
        while l<=r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l +=1
            else:
                res.append(nums[r] * nums[r])
                r -= 1
        return res[::-1] # reverse
        # for i in range(len(nums))
        # n = len(nums)
        # res = []
        # for i in range(len(nums)):
        #     ans = nums[i] * nums[i]
        #     res.append(ans)
        # res.sort()
        # return res