class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        def isAnagram(s1: str, s2: str) -> bool:
            return sorted(s1) == sorted(s2)
        
        for i in range(len(s2) - len(s1) + 1):
            if isAnagram(s1, s2[i:i + len(s1)]):
                return True
        return False