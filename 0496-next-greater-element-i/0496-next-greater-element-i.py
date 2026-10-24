class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d=defaultdict(lambda:-1)
        st=[]
        for i in nums2:
            while st and i>st[-1]:
                d[st.pop()]=i
            st.append(i)
        return [d[i] for i in nums1]

        