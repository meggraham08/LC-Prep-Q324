class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ans = 0
        for num in nums:
            if nums[ans] < num:
                print(nums[ans] ,  num)
                ans += 1
        return ans
