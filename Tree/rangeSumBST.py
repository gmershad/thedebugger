# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        output = []
        if root==None:
            return 0
        
        self.inOrderTraversal(root,low,high,output)
        return sum(output) 
    
    def inOrderTraversal(self, root,low,high,output):
        if root == None:
            return
		
        self.inOrderTraversal(root.left, low,high,output)
		
        if low <= root.val <= high:
            output.append(root.val)
			
        self.inOrderTraversal(root.right, low,high,output)
        
