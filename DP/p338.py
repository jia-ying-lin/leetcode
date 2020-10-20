class Solution:
    """
    Runtime: 84 ms, faster than 74.18% of Python3 online submissions for Counting Bits.
    Memory Usage: 20.7 MB, less than 93.92% of Python3 online submissions for Counting Bits.
    """
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        elif num == 2:
            return [0, 1, 1]
        ans=[0, 1, 1]
        n = 2
        i = 3
        while i <= num:
            if i == n*2:
                ans.append(1)
                i += 1
                n *= 2
                continue
            ans.append(ans[n] + ans[i-n])
            i += 1
        return ans