class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.array = [0] * k
        self.rear = -1
        self.size = 0
        self.capacity = k
        
    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = value
        self.size += 1
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        self.size -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        
        return self.array[(self.rear - self.size + 1) % self.capacity]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty(): 
            return -1
        
        return self.array[self.rear]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return not self.size
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
