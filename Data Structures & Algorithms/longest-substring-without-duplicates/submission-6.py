class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_list = []
        longest = 0
        for i in range(len(s)):
            if s[i] in char_list:
                longest = max(longest, len(char_list))
                while s[i] in char_list:
                    char_list.pop(0)
            char_list.append(s[i])
        longest = max(longest, len(char_list))
        return longest
        