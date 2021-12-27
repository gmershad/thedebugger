# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.traverse = []
        self.inOrder(root)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.traverse.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.traverse) != 0:
            return True
        
        return False
    
    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            self.traverse.append(node.val)
            self.inOrder(node.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
