class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(list(map(len, strs)))
        res = ""
        for i in range(min_length):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return res
            res += char
        return res