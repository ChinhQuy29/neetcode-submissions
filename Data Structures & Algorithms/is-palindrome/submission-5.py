class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        def helper(l: int, r: int) -> bool:
            if l >= r:
                return True
            
            if cleaned[l] != cleaned[r]:
                return False
            
            return helper(l + 1, r - 1)
        
        return helper(0, len(cleaned) - 1)