# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left == None and root.right == None:
            return True
        l_stack = [root.left]
        r_stack = [root.right]
        while len(l_stack) > 0 and len(r_stack) > 0:
            l = l_stack.pop()
            r = r_stack.pop()
            
            if l != None and r != None:
                if l.val == r.val:
                    l_stack.append(l.left)
                    l_stack.append(l.right)
                    r_stack.append(r.right)
                    r_stack.append(r.left)
                else:
                    return False
            elif not(l == None and r == None):
                return False
        if len(l_stack) > 0 or len(r_stack) > 0 :
            return False
        return True
            
        