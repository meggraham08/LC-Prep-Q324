class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        #  0  1  2  3   4  5
        # [ 1, 1, 2, 2, 4 ,4 ]
        #   i
        #         j
        i = 0
        j = 0
        while j < len(nums):
            print("i", i, "nums[i]", nums[i])
            print("j", j , "nums[j]", nums[j])
            if nums[i] == nums[j]:
                j += 1
                print("j again", j)
            else:
                print("IN ELSE!! i", i, "nums[i]", nums[i])
                print("in else!!!!! j", j , "nums[j]", nums[j])
                nums[i+1] = nums[j]
                count += 1
                i += 1
            # i = j
        print(count)
        return count + 1

        # my_dict = {}
        # for i in range(len(nums)):
        #     if nums[i] not in my_dict:
        #         my_dict[nums[i]] = i
        #     # else:
        #     #     my_dict[nums[i]] += i
        # print(my_dict)

        # [1 , 1, 2]
        # left = 0 
        # right = len(nums)
        # while left < right:
        #     if nums[left] != nums[right - 1]:
        #         nums[left] = nums[right -1]
        #         right -= 1
        #     else:
        #         left += 1
        # return right