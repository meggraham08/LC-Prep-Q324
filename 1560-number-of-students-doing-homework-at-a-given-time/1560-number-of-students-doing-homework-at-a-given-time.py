class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # [ 1, 2, 3 ].        [ 3, 2, 7 ]
        # 
        # loop through startTime and loop through endTime,
        # if query time is in between the range for nums1[i] and nums2[i]
        # count += 1
        count = 0
        # can do this because startTime.len is the same as endTime.len
        for i in range(len(startTime)):
            # this is literally checkinf if its in the range
            # so is 1 < = queryTime <= 3:
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count