class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        df=[-1]*(n+1)
        return self.calculate(n,df)
    def calculate(self,n,df):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif df[n]!=-1:
            return df[n]
        else:
            df[n]=self.calculate(n-1,df)+self.calculate(n-2,df)+self.calculate(n-3,df)
        return df[n]
        