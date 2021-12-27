# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        self.result = []
        if root1 != None:
            self.dfs(root1)
        
        if root2 != None:
            self.dfs(root2)
        
        return sorted(self.result)
        
    def dfs(self, root):
        self.result.append(root.val)
        if root.left != None:
            self.dfs(root.left)
        
        if root.right != None:
            self.dfs(root.right)
        
        
        
        
        
