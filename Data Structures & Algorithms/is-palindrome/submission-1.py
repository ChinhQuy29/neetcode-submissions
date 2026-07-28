class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s = ""
        for char in s:
            if char.isalnum():
                alnum_s += char.lower()
        return alnum_s == alnum_s[::-1]