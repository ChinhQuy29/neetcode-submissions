class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        used = [False] * len(nums)

        def backtrack():
            if len(perm) == len(nums) and perm not in res:
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                perm.append(nums[i])
                backtrack()
                perm.pop()
                used[i] = False

        backtrack()
        return res