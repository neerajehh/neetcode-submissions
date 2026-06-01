"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        max_count = 0 
        count=0

        for i in intervals:
            start.append(i.start)
        start.sort()
        end = []
        for i in intervals:
            end.append(i.end)
        end.sort()
        i = 0 
        j = 0 
        while i<len(intervals): 

         if start[i]<end[j]:
            i+=1
            count+=1
            max_count = max(count,max_count)
         else:
            j+=1
            count-=1
        return max_count