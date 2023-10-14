class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        temp = 0
        count = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[temp][1]:
                temp = i
                count += 1

        return len(intervals) - count
