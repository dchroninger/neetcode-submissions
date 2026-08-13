class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        scounts = {}
        tcounts = {}
        for sl in s:
            if sl not in t: return False
            scounts[sl] = scounts.get(sl,0) + 1

        for tl in t:
            if tl not in s: return False
            tcounts[tl] = tcounts.get(tl,0) + 1

        for k in scounts.keys():
            if scounts[k] != tcounts[k]: return False
        
        return True