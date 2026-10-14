class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            l=target-nums[i]
            if l in nums and nums.index(l)!=i:
                return [i,nums.index(l)]
        