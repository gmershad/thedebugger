# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dp = {}
        return self.solve(root, dp)
    
    def solve(self, root, dp):
        if not root:
            return 0
        
        if root in dp:
            return dp[root]
        
        val = 0
        if root.left:
            val += self.solve(root.left.left, dp) + self.solve(root.left.right, dp)
        
        if root.right:
            val += self.solve(root.right.left, dp) + self.solve(root.right.right, dp)
        
        val = max(val + root.val, self.solve(root.left, dp) + self.solve(root.right, dp))
        dp[root] = val
        
        return val
    
    
            
