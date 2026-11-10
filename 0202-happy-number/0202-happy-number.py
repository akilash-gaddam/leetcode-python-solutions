class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        i=0
        if n == 1:
            return True
        elif n == 4:
            return False
        while(n>0):
            i=n%10
            i=i**2
            s=s+i
            n=n//10
        return self.isHappy(s)        