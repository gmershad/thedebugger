import math

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                b = s.pop()
                a = s.pop()
                if t == "+":
                    s.append(a + b)
                if t == "-":
                    s.append(a - b)
                if t == "*":
                    s.append(a * b)
                if t == "/":
                    s.append(int(float(a)/b))
            else:
                s.append(int(t))
        return s.pop()
