class Solution:
    '''
    O(n^2)
    naive solution
    '''
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for cur in nums:
            count = 0
            for n in nums:
                if n < cur:
                    count += 1
            ans.append(count)
        return ans
    '''
    O(nlogn)
    Big O of sorted is nlogn
    '''
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        for i, n in enumerate(sorted(nums)):
            count.setdefault(n, i)
        return [count[num] for num in nums]