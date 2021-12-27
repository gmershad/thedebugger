# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.preOrder = []
        total = self.subTreeSum(root)
        ans = 0
        
        for partial in self.preOrder:
            candid = (total - partial) * partial
            if candid > ans:
                ans = candid
        
        return ans % (10 ** 9 + 7)
        
    
    def subTreeSum(self, node):
        s = node.val
        
        if node.left:
            s += self.subTreeSum(node.left)
        
        if node.right:
            s += self.subTreeSum(node.right)
        
        self.preOrder.append(s)
        return s
        
        
