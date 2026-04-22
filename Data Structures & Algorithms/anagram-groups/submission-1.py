class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = defaultdict(list)
        for strr in strs:
            key = "".join(sorted(strr))
            a_map[key].append(strr)
        return list(a_map.values())

