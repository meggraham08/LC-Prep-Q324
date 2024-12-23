class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in my_map:
                return [index, my_map[complement]]
            my_map[num] = index

