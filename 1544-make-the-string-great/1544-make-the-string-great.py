class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        stack=[]
        top = -1
        for i in s:
            if stack and abs(ord(i)-ord(stack[top]))==32:
                stack.pop()
                top-=1
            else:
                stack.append(i)
                top+=1
        return "".join(stack)

        



        