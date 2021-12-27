# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev_node = None
        self.first_node = None
        self.second_node = None
        self.inOrder(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val
        
    
    def inOrder(self, root):
        if not root:
            return 
        
        self.inOrder(root.left)
        
        if self.prev_node and self.prev_node.val > root.val:
            if not self.first_node:
                self.first_node = self.prev_node
            
            self.second_node = root
        
        self.prev_node = root
        self.inOrder(root.right)
        
        
    
        
            
        
