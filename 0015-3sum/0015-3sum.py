class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        my_list = []
        for i in range(len(nums) - 2):
            # this is checking that i is larger than target and if eles are the same
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left = i + 1
            right = len(nums) - 1
            while left < right:
                my_sum = nums[i] + nums[left] + nums[right]
                if my_sum == 0:
                    my_list.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif my_sum > 0:
                    right -= 1
                else:
                    left += 1

        return my_list

        # my_map { res: i, }
        # my_map { 3: 0, 4: 1, 2:2 }

        # my_map = {}
        # nums.sort()
        # sum_list = []
        # for i in range(len(nums)):
        #     a = nums[0]
        #     res = a + nums[i]
        #     if res == 0:
        #         if nums[i] in my_map:
        #             return [i, my_map[nums[i]]]
        #     my_map[res] = i 
        #     print(my_map)


        # for i, val_i in enumerate(nums):
        #     if i > 0 and val_i
        #     for j, val_j in enumerate(nums):
        #         if j <= i:
        #             continue
        #     # if val_i > 0 and 
        #     print(i, j)


        # not optimal (O(n^3))
        # temp_sum = 0
        # sum_list = []
        # for i, val_i in enumerate(nums):
        #     for j, val_j in enumerate(nums):
        #         for k, val_k in enumerate(nums):
        #             if j <= i:
        #                 continue
        #             if k <= j:
        #                 continue
        #             temp_sum = val_i + val_j + val_k
        #             if temp_sum == 0:
        #                 triple = sorted([val_i, val_j, val_k])
        #                 if triple not in sum_list:
        #                     sum_list.append(triple)

        # return sum_list
        # i , j , k = 0 , 1 , 2
        # while k <= len(nums)-1:
        #     if nums[i] != nums[j]:

        