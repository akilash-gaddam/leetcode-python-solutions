class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        for i in s:
            if stack and ord(stack[-1]) - ord(i) == -1 and stack[-1]+i in ["AB","CD"]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
            
        