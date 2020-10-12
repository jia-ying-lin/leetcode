class Solution:
    """
    Runtime: 32 ms, faster than 86.52% of Python3 online submissions for Unique Number of Occurrences.
    Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Unique Number of Occurrences.
    """
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = {}
        for i in arr:
            if i not in h:
                h[i] = 1
            else:
                h[i] = h[i] + 1
        return len(h.keys()) == len(set(h.values()))