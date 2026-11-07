class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=min(nums)
        l=max(nums)
        n=[]
        for i in range(s,l+1):
            if i not in nums:
                n.append(i)
        return n

        