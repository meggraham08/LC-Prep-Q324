class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        l, r = 0, len(numbers) - 1

        # need loop to iterate over array
        while l < r:
            #defining current sum taking element of the pointers
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []