class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        out = []

        for s in strs:
            key = str(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        
        for v in groups.values(): out.append(v)
        return out
