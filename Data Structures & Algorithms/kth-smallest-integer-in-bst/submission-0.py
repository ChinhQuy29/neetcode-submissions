# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return root
        
        arr = []
        def inorder(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return root
                
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        
        inorder(root)
        return arr[k - 1]