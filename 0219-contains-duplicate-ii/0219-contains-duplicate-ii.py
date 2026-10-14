class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict={}
        for i,n in enumerate(nums):
            if  n in dict and i-dict[n]<=k:
                return True
            dict[n]=i
        return False
            

        


            