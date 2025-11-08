from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            chars = sorted(s)
            key = ''.join(chars)
            res[key].append(s)
        return list(res.values())

