class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s=sum(nums[:k])
        m=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            m=max(s,m)
        return float(m)/k
        