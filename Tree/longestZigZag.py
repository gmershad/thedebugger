# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.finalMax = 0
        self.helper(root.left, False, 0)
        self.helper(root.right, True, 0)
        
        return self.finalMax
        
    
    def helper(self, root, isNextLeftMove, currentMax):
        if not root:
            self.finalMax = max(currentMax, self.finalMax)
            return
        
        if isNextLeftMove:
            self.helper(root.left, False, currentMax + 1)
            self.helper(root.right, True, 0)
        else:
            self.helper(root.left, False, 0)
            self.helper(root.right, True, currentMax + 1)
            
            
