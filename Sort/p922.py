class Solution:
    """
    Time: O(n)
    Space: O(n)
    Runtime: 188 ms, faster than 99.71% of Python3 online submissions for Sort Array By Parity II.
    Memory Usage: 16.6 MB, less than 32.04% of Python3 online submissions for Sort Array By Parity II.
    """
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = 0
        odd = 1
        ans = [0]*len(A)
        for n in A:
            if n % 2 == 0:
                ans[even] = n
                even += 2
            else:
                ans[odd] = n
                odd += 2
        return ans
    """
    for every misplaced odd there is misplaced even
    Runtime: 204 ms, faster than 92.11% of Python3 online submissions for Sort Array By Parity II.
    Memory Usage: 16.3 MB, less than 32.04% of Python3 online submissions for Sort Array By Parity II.
    """
    class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = 0
        odd = 1
        l = len(A)
        while even < l and odd < l:
            if A[even] % 2 == 0:
                even += 2
            elif A[odd] % 2 == 1:
                odd += 2
            elif A[even] % 2 == 1 and A[odd] % 2 == 0:
                A[even], A[odd] = A[odd], A[even]
                even += 2
                odd += 2
        return A
