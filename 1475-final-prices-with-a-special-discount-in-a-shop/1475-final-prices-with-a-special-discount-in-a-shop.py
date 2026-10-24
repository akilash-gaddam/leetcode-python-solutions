class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        arr=[]
        for i in range(len(prices)):
            l=len(arr)
            for j in range(i,len(prices)):
                if prices[i]>=prices[j] and j > i:
                    arr.append(prices[i]-prices[j])
                    break
            if len(arr) == l:
                arr.append(prices[i])
        return arr
        