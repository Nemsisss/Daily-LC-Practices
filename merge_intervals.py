class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based on the second element of the interval
        intervals=list(sorted(intervals, key= lambda x:x[1]))
        for i in range(len(intervals)-1, 0, -1):
            if intervals[i][0]<=intervals[i-1][1] :
                intervals[i-1]= [min(intervals[i-1][0], intervals[i][0]), intervals[i][1] ]
                del intervals[i]
                
        return intervals
