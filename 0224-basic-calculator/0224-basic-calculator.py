class Solution(object):
    def calculate(self, s):
        stk=[]
        result,num,sign = 0,0,1
        for _ in s:
            if _.isdigit():
                num=num* 10 +int(_)
            elif _ in ['+','-']:
                result += sign * num
                num = 0
                sign = 1 if _ == '+' else -1
            elif _ == '(':
                stk.append(result)
                stk.append(sign)
                result,sign=0,1
            elif _ == ")":
                result+=sign * num
                num=0
                result *= stk.pop()
                result += stk.pop()

        return result+sign*num
        