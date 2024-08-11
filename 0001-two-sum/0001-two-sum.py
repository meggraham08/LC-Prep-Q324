class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # left = 0
        # right = len(nums) - 1

        # while left < right:
        #     sum = nums[left] + nums[right]
        #     if sum == target:
        #         return [left, right]
        #     elif sum > target:
        #         right -= 1
        #     else:
        #         left += 1
        # return []
        # my_map { res: i, }
        # my_map { 3: 0, 4: 1, 2:2 }

        my_map = {}
        for i, val_i in enumerate(nums):
            res = target - val_i
            # print(i, val_i, my_map, res)
            if val_i in my_map:
                # shows the val exists in map
                return [i, my_map[val_i]]
            my_map[res] = i 

            
    # [ 3 , 2, 4]
    # O(n^2)
        # temp_sum = 0
        # for i, val_i in enumerate(nums):
        #     for j, val_j in enumerate(nums):
        #         if j <= i:
        #             continue
        #         temp_sum = val_i + val_j
        #         if target == temp_sum:
        #             return [i,j]
                # else:
                #     return []
                
        

