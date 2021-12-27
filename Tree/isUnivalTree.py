# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    to_return = True
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        
        return left_correct and right_correct
