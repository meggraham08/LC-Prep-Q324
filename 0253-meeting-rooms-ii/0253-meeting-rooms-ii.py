class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key= lambda x: x[0])
        meetingRooms = []
        heapq.heappush(meetingRooms, intervals[0][1])
        for i in intervals[1:]:
            if meetingRooms[0] <= i[0]:
                heapq.heappop(meetingRooms)
            heapq.heappush(meetingRooms,i[1])
        return len(meetingRooms)
            