class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []

        if len(nums) == 1:
            return nums[0]
        else:
            for i in nums:
                if i not in seen:
                    seen.append(i)
                else:
                    seen.remove(i)
            return seen.pop()
