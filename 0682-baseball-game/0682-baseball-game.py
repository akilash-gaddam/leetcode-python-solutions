class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        top=-1
        for i in operations:
            if i == "+":
                stack.append(stack[top]+stack[top-1])
                top+=1
            elif i =="C":
                top-=1
                stack.pop()
            elif i == "D":
                stack.append(stack[top]*2)
                top+=1
            else:
                stack.append(int(i))
                top+=1

        t=sum(stack)
        return t
        