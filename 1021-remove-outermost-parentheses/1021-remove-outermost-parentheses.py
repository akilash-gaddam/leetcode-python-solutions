class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        c=0
        c1=0
        for i in range(len(s)):
            if s[i] == "(":
                if c > c1:
                    stack.append(s[i])
                c+=1
            elif s[i]==")":
                c1+=1
                if c>c1:
                    stack.append(s[i])
                
        return "".join(stack)



        