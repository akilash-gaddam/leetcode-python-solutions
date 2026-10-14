import random
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num=nums1+nums2

        def quick(nums):
            if len(nums)<=1:
                return nums
            pivot=random.choice(nums)

            left=[x for x in nums if x < pivot]
            middle =[x for x in nums if x == pivot]
            right=[x for x in nums if x > pivot]
            return quick(left) + middle + quick(right)
        num=quick(num)
        n=len(num)
        if n%2 == 0:
            return (num[(n//2)-1]+num[(n//2)])/2.0
        return num[n//2]