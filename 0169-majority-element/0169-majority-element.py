class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majEle = len(nums) // 2
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, val in count.items():
            if val > majEle:
                return key