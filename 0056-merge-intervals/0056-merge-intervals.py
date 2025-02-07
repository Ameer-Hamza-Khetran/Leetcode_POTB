class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # Sort intervals in-place by start time
        k = 0  # Position of the last merged interval
        
        for i in range(1, len(intervals)):  # Start from the second interval
            if intervals[k][1] >= intervals[i][0]:  # Overlapping intervals
                intervals[k][1] = max(intervals[k][1], intervals[i][1])  # Merge in-place
            else:
                k += 1  # Move forward
                intervals[k] = intervals[i]  # Overwrite interval at k
        
        return intervals[:k + 1]  # Return only merged intervals
