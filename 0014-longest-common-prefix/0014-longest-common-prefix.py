class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Find the shortest string to minimize unnecessary iterations
        shortest = min(strs, key=len)
        
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    # Mismatch found, return up to the current index
                    return shortest[:i]
                    
        return shortest