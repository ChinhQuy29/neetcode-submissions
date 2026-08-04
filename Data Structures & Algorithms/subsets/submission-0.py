class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []

        def backtrack(start: int) -> None:
            res.append(current.copy())

            for i in range(start, len(nums)):
                current.append(nums[i])

                backtrack(i + 1)

                current.pop()
        
        backtrack(0)
        return res