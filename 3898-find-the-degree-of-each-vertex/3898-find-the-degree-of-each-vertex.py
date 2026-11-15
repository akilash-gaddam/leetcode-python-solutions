class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # n=len(matrix)
        # deg=[]
        # for i in range(n):
        #     d=0
        #     for j in range(n):
        #         if (matrix[i][j] == 1):
        #             d+=1
        #     deg.append(d)
        #     d=0
        # return deg

        deg=[0]*len(matrix)
        deg=[sum(i) for i in matrix]
        return deg
        