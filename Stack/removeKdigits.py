class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num=list(num)
        stack,i=[num[0]],1
        
        while i<len(num):
            while stack and k>0 and num[i]<stack[-1]:
                stack.pop()
                k-=1
                
            stack.append(num[i])
            i+=1
            
        while k>0:
            stack.pop()
            k-=1
        stack="".join(stack)
        return stack.lstrip("0") if stack!="" and int(stack)!=0 else "0"
