# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # Tag each node with it's depth
        self.depth = {None: -1}
        self.dfs(root)
        self.maxDepth = max(self.depth.itervalues())
        
        return self.answer(root)
        
    
    def dfs(self, node, parent=None):
        if node:
            self.depth[node] = self.depth[parent] + 1
            self.dfs(node.left, node)
            self.dfs(node.right, node)
        
    def answer(self, node):
        if not node or self.depth.get(node, None) == self.maxDepth:
            return node
        
        l = self.answer(node.left)
        r = self.answer(node.right)
        
        return node if l and r else l or r
    
        
