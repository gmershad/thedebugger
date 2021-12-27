# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.num = 0
        self.dfs(root, float('-inf'))
        return self.num
        
    
    def dfs(self, root, curMax):
        if root == None:
            return
        
        if root.val >= curMax:
            self.num += 1
            curMax = root.val
            
        self.dfs(root.left, curMax)
        self.dfs(root.right, curMax)
        
        return self.num
