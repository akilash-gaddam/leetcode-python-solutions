class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix={0:1}
        c_sum=0
        sub=0
        for i in nums:
            c_sum+=i
            if (c_sum - k) in prefix:
                sub+=prefix[c_sum - k]
            prefix[c_sum] = prefix.get(c_sum,0)+1
        return sub
        

        