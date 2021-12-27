# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = []
        self.inOrder(root, k)
        return self.res.pop()
    
    def inOrder(self, root, k):
        if not root:
            return
        
        self.inOrder(root.left, k)
        if len(self.res) == k:
            return
        
        self.res.append(root.val)
        self.inOrder(root.right, k)
        
        
