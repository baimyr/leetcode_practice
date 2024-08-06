class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        for a_str in strs:
            letters = tuple(sorted(a_str))
            anag[letters].append(a_str)
        return anag.values()