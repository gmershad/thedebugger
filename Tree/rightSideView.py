# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, node, currLevel, res):
        if not node:
            return
        
        if currLevel >= len(res):
            res.append(node.val)
        
        if node.right:
            self.dfs(node.right, currLevel+1, res)
        
        if node.left:
            self.dfs(node.left, currLevel+1, res)
