class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sub_string = s[0]
        max_length = 1
        for i in range(len(s)):
            for j in range(len(sub_string)):
                if s[i] == sub_string[j] and j == len(sub_string) - 1:
                    sub_string = ""
                    break
                elif s[i] == sub_string[j] and j < len(sub_string) - 1:
                    sub_string = sub_string[j + 1:]
                    break
            sub_string += s[i] 
            max_length = max(len(sub_string), max_length)
        return max_length