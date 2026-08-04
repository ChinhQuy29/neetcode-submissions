class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def isValid(s):
            balance = 0
            for c in s:
                balance += 1 if c == "(" else -1
                if balance < 0:
                    return False
            
            return not balance

        def dfs(s):
            if len(s) == 2 * n:
                if isValid(s):
                    res.append(s)
                return
            
            dfs(s + "(")
            dfs(s + ")")
        
        dfs("")
        return res