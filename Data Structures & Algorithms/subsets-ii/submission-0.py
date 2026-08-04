class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtrack(start: int) -> None:
            if subset not in res:
                res.append(subset.copy())
            
            for i in range(start, len(nums)):
                subset.append(nums[i])

                backtrack(i + 1)

                subset.pop()

        backtrack(0)
        return res