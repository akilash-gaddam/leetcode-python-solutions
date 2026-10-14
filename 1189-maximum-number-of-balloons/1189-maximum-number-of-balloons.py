class Solution(object):
    def maxNumberOfBalloons(self, text):
        count=[0]*5
        for i in text:
            if i == "b" : count[0]+=1
            elif i =="a" : count[1]+=1
            elif i == "l": count[2]+=1
            elif i == "o": count[3]+=1
            elif i == "n": count[4]+=1
        
        count[2]=count[2]//2
        count[3]=count[3]//2
        return min(count)