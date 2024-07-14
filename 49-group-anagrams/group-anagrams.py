class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=defaultdict(list)
        k=""
        for u in strs:
            s=k.join(sorted(u))
            h[s].append(u)
        return sorted(h.values())
        