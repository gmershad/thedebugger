# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        traversal = []
        self.inOrder(root, traversal)
        return self.binaryTraverse(traversal, 0, len(traversal) - 1)
    
    def inOrder(self, root, traverse):
        if not root:
            return
        
        self.inOrder(root.left, traverse)
        traverse.append(root.val)
        self.inOrder(root.right, traverse)
        
        return 
    
    def binaryTraverse(self, arr, left, right):
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        node = TreeNode(arr[mid])
        node.left = self.binaryTraverse(arr, left, mid-1)
        node.right = self.binaryTraverse(arr, mid+1, right)
        
        return node
    
    
        
