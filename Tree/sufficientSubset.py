# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        return self.helper(root, limit, 0)
    
    def helper(self, root, limit, pathSum=0):
        if root == None:
            return None
        
        if root.left == None and root.right == None:
            if (pathSum + root.val) < limit:
                return None
            
            return root
        
        root.left = self.helper(root.left, limit, (pathSum + root.val))
        root.right = self.helper(root.right, limit, (pathSum + root.val))
        
        if root.left == None and root.right == None:
            return None
        
        return root
        
