# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.dfs(root)
        return root
        
    def dfs(self, root):
        if root == None:
            return
        
        self.dfs(root.right)
        self.sum = self.sum + root.val
        root.val = self.sum
        
        self.dfs(root.left)
        
