# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        node = TreeNode(val)
        if self.root:
            parent, _ = self.getParent(self.root)
            
            if not parent.left:
                parent.left = node
            else:
                parent.right = node
            
            val = parent.val
        else:
            self.root = node
        
        return val
            
        

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
    
    def getParent(self, root, level=0):
        if root:
            if not root.left:
                return (root, level)
            
            if not root.right:
                return (root, level)
            
            parentLeft, levelLeft = self.getParent(root.left, level+1)
            parentRight, levelRight = self.getParent(root.right, level+1)
            
            if levelLeft <= levelRight:
                return (parentLeft, levelLeft)
            else:
                return (parentRight, levelRight)
            
        
        return (root, level)
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
