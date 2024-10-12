class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # [ 1, 2, 3 ].        [ 3, 2, 7 ]
        # 
        # 
        # 
        # loop through i and loop through j, if query time is in between the range for nums1[i] and nums2[i]
        # count += 1
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count