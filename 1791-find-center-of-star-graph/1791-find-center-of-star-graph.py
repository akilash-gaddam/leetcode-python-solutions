class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges[0][0] == edges[1][0]:
            return edges[0][0]
        elif edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]
        
        