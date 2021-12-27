# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None or root2 is None:
            return root1 == root2
        
        return self.leaf_value_sequence(root1) == self.leaf_value_sequence(root2)
    
    def leaf_value_sequence(self, node):
        leaf_values = []
        
        if node.left is None and node.right is None:
            return [node.val]
        
        if node.left:
            leaf_values.extend(self.leaf_value_sequence(node.left))
        
        if node.right:
            leaf_values.extend(self.leaf_value_sequence(node.right))
            
        return leaf_values

        
