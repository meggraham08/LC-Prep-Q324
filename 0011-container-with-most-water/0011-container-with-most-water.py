class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0 
        right = len(height) - 1
        while left < right:
            width = right - left
            max_area = max(max_area, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area






        # we know base * height
        # can't sort it
        # brute force 
        # create a res hash key is the index + 1 and then values are a list of the maxAreas
        # loop through array with start and end pointer
        # get max amoutn of range of start and end and the median both 
        # add index + 1 to key in hash and t
        # ie. 1 , 8, -- you can only do 1 to 1, and 1 in between is 1, so it would be 1 * 1
        # also if start is greater than end, skip
        # my_hash {
        #     1: [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #     2: [6, 6, 15, 20, 48, 27, 49]
        #     3: [4, 15, 16, 30, 18, 42]
        #     4: [ 2, 4, 6, 8, 10]
        #     5: [4, 10, 12, 25]
        #     6: [4, 9 , 16]
        #     7: [3, 14]
        #     8: [3]
        # }
        # one of the two values needs to be in the range of the other and it need to be before it
        # max_area = 0
        # for start, val_start in enumerate(height):
        #     for end, val_end in enumerate(height):
        #         val_height = 1
        #         if end <= start:
        #             continue
        #         base = end - start
        #         max_area = max(max_area, min(val_start, val_end) * base)
        # return max_area

        

        