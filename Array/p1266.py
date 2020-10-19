class Solution:
    """
    Runtime: 52 ms, faster than 96.37% of Python3 online submissions for Minimum Time Visiting All Points.
    Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.
    """
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        s = points[0]
        t = 0
        for p in points[1:]:
            t += max(abs(p[0]-s[0]), abs(p[1]-s[1]))
            s = p
        return t