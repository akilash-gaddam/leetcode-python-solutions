class Solution(object):
    def groupAnagrams(self, strs):
        ana=defaultdict(list)
        for s in strs:
            sorted_s=tuple(sorted(s))
            ana[sorted_s].append(s)

        return ana.values()