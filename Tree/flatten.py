# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None or root.left == None and root.right == None:
            return None
        
        if root.left != None:
            self.flatten(root.left)
            
            tmpRight = root.right
            root.right = root.left
            root.left = None
            
            t = root.right
            while t.right != None:
                t = t.right
            
            t.right = tmpRight
            
        self.flatten(root.right)
        
            
        
        
