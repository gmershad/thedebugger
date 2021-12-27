# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if root:
            c = self.helper(root, targetSum)
            l = self.pathSum(root.left, targetSum)
            r = self.pathSum(root.right, targetSum)
            return (c + l + r)
        
        return 0
    
    def helper(self, root, summ):
        if root:
            l = self.helper(root.left, summ - root.val)
            r = self.helper(root.right, summ - root.val)
            val = 0
            if root.val == summ:
                val = 1
                
                
            
            return (l + r + val)
        
        return 0
        
