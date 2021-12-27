class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        x = self.q.pop()
        return x
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.q) == 0:
            return -1
        
        return self.q[- 1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()