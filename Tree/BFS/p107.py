# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 36 ms, faster than 62.03% of Python3 online submissions for Binary Tree Level Order Traversal II.
    Memory Usage: 14.3 MB, less than 16.09% of Python3 online submissions for Binary Tree Level Order Traversal II.
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q=[[root]]
        t=[]
        while q:
            n = q.pop(0)
            l=[]
            q_l=[]
            for node in n:
                l.append(node.val)
                if node.left :
                    q_l.append(node.left)
                if node.right:
                    q_l.append(node.right)
            if q_l:
                q.append(q_l)
            t.append(l)
        return t[::-1]
            
        