# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.trav(root, None, None)
        return self.sum
    
    def trav(self, root, parent, grandParent):
        if grandParent and (grandParent % 2 == 0):
            self.sum += root.val
        
        if root.left:
            self.trav(root.left, root.val, parent)
        
        if root.right:
            self.trav(root.right, root.val, parent)
        
        
