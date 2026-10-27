class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        a=x
        while a>0:
            s+=a%10
            a=a//10
        if (x % s == 0):
            return s
        return -1

        