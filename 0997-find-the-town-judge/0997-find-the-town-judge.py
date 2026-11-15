class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        ind=[0]*(n+1)
        oud=[0]*(n+1)

        for i in trust:
            oud[i[0]]+=1
            ind[i[1]]+=1
        for i in range(1,n+1):
            if ind[i] == (n-1) and oud[i]== 0:
                return i
        return -1