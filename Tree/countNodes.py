# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.preOrder(root)
    
    def preOrder(self, root):
        if root:
            return 1 + self.preOrder(root.left) + self.preOrder(root.right)
        else:
            return 0
        
