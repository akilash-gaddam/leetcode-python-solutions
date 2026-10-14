class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target in nums:
            return 1
        l=0
        r=0
        s=0
        ms=len(nums)+1
        m=0
        while(r<len(nums)):
            s+=nums[r]
            while s>=target:
                m=r-l+1
                ms=min(ms,m)
                s-=nums[l]
                l+=1
            r+=1
        if ms > len(nums):
            return 0
        return ms
        