class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        i=0
        j=0
        while (i<len(pushed) and j < len(popped)):
            stack.append(pushed[i])
            i+=1
            while stack and stack[-1] == popped[j] and j<len(popped) :
                    stack.pop()
                    j+=1

        if stack==[]:
            return True
        return False

            
        