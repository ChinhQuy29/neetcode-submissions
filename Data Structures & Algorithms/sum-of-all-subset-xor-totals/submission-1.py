class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        subset = []

        def dfs(start):
            nonlocal res

            tmp = 0
            for num in subset:
                tmp ^= num
            res += tmp

            for i in range(start, len(nums)):
                subset.append(nums[i])

                dfs(i + 1)

                subset.pop()

        dfs(0)
        return res