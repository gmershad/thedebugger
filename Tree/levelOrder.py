# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        return self.preOrder(root, 0, res)
    
    def preOrder(self, node, level, res):
        if node:
            if len(res) < level + 1:
                res.append([])
            
            res[level].append(node.val)
            self.preOrder(node.left, level+1, res)
            self.preOrder(node.right, level+1, res)
            
        return res
            
