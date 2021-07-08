# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        s = [root]
        ans = []
        while len(s) != 0:
            now = s.pop()
            if now.left:
                s.append(now)
                s.append(now.left)
                now.left = None
            else:
                ans.append(now.val)
                if now.right:
                    s.append(now.right)
                    now.right = None
        return ans                