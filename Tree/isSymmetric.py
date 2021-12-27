# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        
        return self.isMirror(root.right, root.left)
    
    def isMirror(self, left, right):
        if (left is None and right is None):
            return True
        
        return (left is not None and right is not None) and (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        
