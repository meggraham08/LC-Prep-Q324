class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majEle = len(nums) // 2
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count)
        for key, value in count.items():
            if value > majEle:
                return key
        