# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBST(root)
        
    def isBST(self, root, l=None, r= None):
        if root == None:
            return True
        
        if (l != None and root.val <= l.val):
            return False
        
        if (r != None and root.val >= r.val):
            return False
        
        return self.isBST(root.left, l, root) and self.isBST(root.right, root, r)
