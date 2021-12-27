# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.fn(root, float('-inf'), float('inf'))
    
    def fn(self, node, lo, hi):
            if not node: return hi - lo
            left = self.fn(node.left, lo, node.val)
            right = self.fn(node.right, node.val, hi)
            return min(left, right)
