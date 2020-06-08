class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def can_merge(interval1, interval2):
            if interval1[1] >= interval2[0] and interval1[0] <= interval2[0]:
                return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
            return None
        intervals = sorted(intervals, key=lambda x:x[0])
        merged_intervals = []
        used_intervals = []
        while intervals:
            interval1 = intervals.pop(0)
            for interval2 in intervals:
                if interval2 in used_intervals:
                    continue
                merged = can_merge(interval1, interval2)
                if merged:
                    interval1 = merged
                    used_intervals.append(interval2)
            intervals = [interval for interval in intervals if interval not in used_intervals]
            merged_intervals.append(interval1)

        return merged_intervals
