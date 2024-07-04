class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]] = i
                print(dict[nums[i]])
            else:
                print([dict[target-nums[i]],i])
                return [dict[target-nums[i]],i]