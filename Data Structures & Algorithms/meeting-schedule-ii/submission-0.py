import heapq
from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort by meeting start time
        intervals.sort(key=lambda interval: interval.start)

        rooms = []  # min-heap storing end times

        for interval in intervals:
            start = interval.start
            end = interval.end

            # Reuse room if earliest meeting ended
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)

            heapq.heappush(rooms, end)

        return len(rooms)