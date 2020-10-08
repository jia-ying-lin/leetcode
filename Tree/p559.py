"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    '''
    Runtime: 48 ms, faster than 58.86% of Python3 online submissions for Maximum Depth of N-ary Tree.
    Memory Usage: 15.6 MB, less than 81.91% of Python3 online submissions for Maximum Depth of N-ary Tree.
    '''
    def maxDepth(self, root: 'Node') -> int:
        max_d = 0
        if not root:
            return max_d
        s = [root]
        d = [1]
        while s:
            n_d = d.pop()
            n = s.pop()
            if n_d > max_d:
                max_d = n_d
            if n.children:
                n_d += 1
                s += [c for c in n.children]
                d += [n_d]*len(n.children)   
        return max_d
        