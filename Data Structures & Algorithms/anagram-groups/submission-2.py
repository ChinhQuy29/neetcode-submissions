class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in group:
                group[sorted_str] = [string]
            else:
                group[sorted_str].append(string)
        return list(group.values())