# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        root = self.buildUtil(inorder, postorder, 0, n-1)
        return root
    
    def buildUtil(self, In, post, strt, end):
        if strt > end:
            return None
        
        newNode = TreeNode(post.pop())
        if strt == end:
            return newNode
        
        index = In.index(newNode.val)
        newNode.right = self.buildUtil(In, post, index+1, end)
        newNode.left = self.buildUtil(In, post, strt, index-1)
        
        return newNode
