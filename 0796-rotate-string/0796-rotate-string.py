class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        l=list(s)
        for i in range(len(s)):
            j=l.pop(0)
            l.append(j)
            if "".join(l) == goal:
                return True
        return False


        