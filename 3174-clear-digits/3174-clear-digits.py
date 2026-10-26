class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            if stack and i.isnumeric():
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        