# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        if root.left is None:
            return (1 + self.minDepth(root.right))
        
        if root.right is None:
            return (1 + self.minDepth(root.left))
        
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
        
