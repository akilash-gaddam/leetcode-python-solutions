class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l=str(x)
        i = 0
        j=len(l)-1
        while(i<=j):
            if l[i] == l[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        