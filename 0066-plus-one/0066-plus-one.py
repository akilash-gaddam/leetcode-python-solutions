class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dig=0
        for i in digits:
            dig+=i
            dig=dig*10     
        dig=(dig//10)+1 
        j=0
        for i in str(dig):
            if j == len(digits):
                digits.append(int(i))
            else:
                digits[j]=int(i)
                j+=1
        return digits