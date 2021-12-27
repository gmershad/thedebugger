# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(0, root)
        
    def helper(self, sum, root):
        if not root:
            return 0
        
        sum = sum * 10 + root.val
        if not root.left and not root.right:
            return sum
        return self.helper(sum, root.left) + self.helper(sum, root.right)
    
        
