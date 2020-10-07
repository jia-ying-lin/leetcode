'''
Given an n-ary tree, return the preorder traversal of its nodes' values.

[In-Order, Pre-Order and Post-Order](https://shubo.io/iterative-binary-tree-traversal/)

- 對binary search tree做inorder traversal就是依序拿取
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        s = [root]
        ans = []
        while s:
            n = s.pop()
            ans.append(n.val)
            '''
            Runtime: 52 ms, faster than 72.37% of Python3 online submissions for N-ary Tree Preorder Traversal.
            Memory Usage: 15.8 MB, less than 20.99% of Python3 online submissions for N-ary Tree Preorder Traversal.
            '''
            if n.children:
                for c in n.children[::-1]:
                    s.append(c)
            '''
            Runtime: 48 ms, faster than 88.24% of Python3 online submissions for N-ary Tree Preorder Traversal.
            Memory Usage: 15.8 MB, less than 20.99% of Python3 online submissions for N-ary Tree Preorder Traversal.
            
            s += [c for c in n.children[::-1] if n.children]
            '''
        return ans