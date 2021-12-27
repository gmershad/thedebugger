# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        toDelete = set(to_delete)
        self.res = []
        self.solve(root, to_delete, True)
        return self.res
        
    def solve(self, node, toDelete, isRoot):
        if not node:
            return None
        
        flag = node.val in toDelete
        if not flag and isRoot:
            self.res.append(node)
            
        node.left = self.solve(node.left, toDelete, flag)
        node.right = self.solve(node.right, toDelete, flag)
        
        return None if flag else node
