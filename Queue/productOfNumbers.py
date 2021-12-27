class ProductOfNumbers(object):

    def __init__(self):
        self.stack = [1]
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.stack = [1]
        else:
            self.stack.append(num * self.stack[-1])
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.stack):
            return 0
        else:
            return self.stack[-1] // self.stack[-(k+1)]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
