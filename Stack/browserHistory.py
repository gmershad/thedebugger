class ListNode:
    def __init__(self, val = 0, prev= None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt
        
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.node = ListNode(homepage)
        self.last = self.node
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.last.nxt = ListNode(url)
        self.last.nxt.prev = self.last
        self.last = self.last.nxt
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.last.prev:
            steps -= 1
            self.last = self.last.prev
        
        return self.last.val

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.last.nxt:
            steps -= 1
            self.last = self.last.nxt
        
        return self.last.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
