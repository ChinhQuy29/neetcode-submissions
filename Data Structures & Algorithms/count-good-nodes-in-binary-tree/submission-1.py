# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node: Optional[TreeNode], path: List[int]):
            nonlocal res

            if not node:
                return
            
            if len(path) == 0 or node.val >= max(path):
                res += 1
            path.append(node.val) 
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
            
        dfs(root, [])
        return res
            
