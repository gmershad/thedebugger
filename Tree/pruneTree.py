# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return root if self.containsOne(root) else None
    
    def containsOne(self, node):
        if not node:
            return False
        
        leftContainsOne = self.containsOne(node.left)
        rightContainsOne = self.containsOne(node.right)
        
        if not leftContainsOne:
            node.left = None
        
        if not rightContainsOne:
            node.right = None
            
        
        return node.val or leftContainsOne or rightContainsOne
    
    
        
