# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right  
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.diameter(root)
        return self.result
    
    def diameter(self, node):
        if not node:
            return 0
        
        left = self.diameter(node.left)
        right = self.diameter(node.right)
        
        self.result = max(self.result, left + right)
        return 1 + max(left, right)
    
     
        
    
