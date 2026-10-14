class Solution(object):
    def strStr(self, haystack, needle):
        l=len(needle)
        i=0
        if needle  not in haystack:
            return -1
        else:
            while True:
                if haystack[i:l] == needle:
                    return i
                else:
                    i+=1
                    l+=1



        