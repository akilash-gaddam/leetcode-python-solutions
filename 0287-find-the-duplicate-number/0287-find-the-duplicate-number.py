class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=set(nums)
        for i in nums:
            if i in n:
                n.remove(i)
            elif i not in n:
                return i
        