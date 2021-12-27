# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root == None:
            return False
        
        return self.compare(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def compare(self, root, subRoot):
        if root == None and subRoot == None:
            return True
        
        if root == None or subRoot == None:
            return False
        
        return (root.val == subRoot.val and self.compare(root.left, subRoot.left)
               and self.compare(root.right, subRoot.right))
