class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid_index = len(nums) // 2
        left = self.sortArray(nums[:mid_index])
        right = self.sortArray(nums[mid_index:])
        sortedVals = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                sortedVals.append(left[left_index])
                left_index += 1
            else:
                sortedVals.append(right[right_index])
                right_index += 1
        sortedVals += left[left_index:]
        sortedVals += right[right_index:]
        return sortedVals