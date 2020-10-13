class Solution:
    """
    Runtime: 100 ms, faster than 97.23% of Python3 online submissions for The K Weakest Rows in a Matrix.
    Memory Usage: 14.3 MB, less than 6.88% of Python3 online submissions for The K Weakest Rows in a Matrix.
    
    Calculating the sum of a row has a time complexity of O(n) and is done m times.
    Python's key function will do a Schwartzian transform and cache the sums. Sorting has a complexity of O(m log m).

    Time complexity: O(n * m + m log m)
    Space complexity: O(m)
    """
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = sorted([ (sum(l), i) for i, l in enumerate(mat) ])
        return [ i[1] for i in counts[:k] ]