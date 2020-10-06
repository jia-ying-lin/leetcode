class Solution:
    '''
    32 ms
    naive solution
    '''
    def freqAlphabets(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "#":
                # pop top 2 and count
                num = int(stack.pop())
                num += 10*int(stack.pop())
                stack.append(num)
            else:
                stack.append(int(i))
        return ''.join([chr(n+96) for n in stack])
    '''
    28 ms
    without join
    '''
    def freqAlphabets(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "#":
                # pop top 2 and count
                num = int(stack.pop())
                num += 10*int(stack.pop())
                stack.append(num)
            else:
                stack.append(int(i))
        ans = ''
        for i in stack:
            ans += chr(i+96)
        return ans