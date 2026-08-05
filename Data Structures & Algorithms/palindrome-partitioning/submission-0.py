class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []
        
        def is_palindrome(s):
            return s == s[::-1]

        def dfs(start):
            if start == len(s):
                res.append(parts.copy())
                return

            for end in range(start + 1, len(s) + 1):
                part = s[start:end]

                if not is_palindrome(part):
                    continue

                parts.append(part)
                dfs(end)
                parts.pop()

        dfs(0)
        return res
            