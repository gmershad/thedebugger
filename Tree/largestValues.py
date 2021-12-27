# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, 0, res)
        return res
    
    def helper(self, node, level, res):
        if not node:
            return
        
        if len(res) <= level:
            res.append(node.val)
        
        res[level] = max(res[level], node.val)
        self.helper(node.left, level+1, res)
        self.helper(node.right, level+1, res)
        
