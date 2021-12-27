# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def arrowLength(node):
            if not node:
                return 0
            
            leftLength = arrowLength(node.left)
            rightLength = arrowLength(node.right)
            leftArrow = rightArrow = 0
            
            if node.left and node.left.val == node.val:
                leftArrow = leftLength + 1
            
            if node.right and node.right.val == node.val:
                rightArrow = rightLength + 1
            
            self.ans = max(self.ans, leftArrow + rightArrow)
            return max(leftArrow, rightArrow)
        
        arrowLength(root)
        return self.ans
            
            
