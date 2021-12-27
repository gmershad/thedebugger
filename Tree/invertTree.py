# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root is None):
            return
        
        q = []
        q.append(root)
        
        while (len(q)):
            # Pop top node from the tree
            curr = q[0]
            q.pop(0)
            
            #Swap left child with right child
            curr.left, curr.right = curr.right, curr.left
            
            if (curr.left):
                q.append(curr.left)
            if (curr.right):
                q.append(curr.right)
                
        return root
            
