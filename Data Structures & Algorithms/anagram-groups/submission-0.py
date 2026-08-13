class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        out = []

        for s in strs:
            if str(sorted(s)) not in groups:
                groups[str(sorted(s))] = []
            groups[str(sorted(s))].append(s)
        
        for v in groups.values(): out.append(v)
        return out
