class Solution:
    """
    Runtime: 36 ms, faster than 89.12% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
    Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
    
    As others have mentioned, the built-in sorting algorithm of Python uses a special version of merge sort, called Timsort, which runs in  𝑛log2𝑛  time
    """
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1]-arr[0]
        for i, n in enumerate(arr[:-1]):
            if ( arr[i+1] - n ) != d:
                return False
        return True
        