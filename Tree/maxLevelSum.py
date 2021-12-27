# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = {}
        self.getSum(root, 1)
        return max(self.d, key=self.d.get)
    
    def getSum(self, root, depth):
        if root:
            if depth in self.d:
                self.d[depth] += root.val
            else:
                self.d[depth] = root.val
            
            self.getSum(root.left, depth+1)
            self.getSum(root.right, depth+1)
            
        
