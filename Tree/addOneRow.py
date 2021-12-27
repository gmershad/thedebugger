# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        return self.add(root, depth , 1, False, val )
    
    def add(self, root, d, depth, isRightChild, v):
        if depth == d:
            tree = TreeNode(v)
            if isRightChild:
                tree.right = root
            else:
                tree.left = root
            
            return tree
        
        if root == None:
            return root
        
        root.left = self.add(root.left, d, depth+1, False, v)
        root.right = self.add(root.right, d, depth+1, True, v)
        return root
    
    
