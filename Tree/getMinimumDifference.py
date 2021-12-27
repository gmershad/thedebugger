# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = self.prev = float("inf")
        self.inOrderTraversal(root)
        return self.ans
     
    def inOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left) 
            self.ans = min(self.ans, abs(self.prev - node.val))
            self.prev = node.val  
            self.inOrderTraversal(node.right)
            
