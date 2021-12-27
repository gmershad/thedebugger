# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        d, n = self.postOrder(root)
        return n
    
    def postOrder(self, root):
        if not root:
            return 0, None
        
        d1, n1 = self.postOrder(root.left)
        d2, n2 = self.postOrder(root.right)
        
        if d1 == d2:
            return (d1 + 1), root
        elif d1 > d2:
            return (d1 + 1), n1
        else:
            return (d2 + 1), n2
        
        
