class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        subset = []

        def dfs(start):
            res.append(subset.copy())

            for i in range(start, len(nums)):
                subset.append(nums[i])

                dfs(i + 1)

                subset.pop()

        dfs(0)
        ans = 0
        for subset in res:
            tmp = 0
            for num in subset:
                tmp ^= num
            ans += tmp

        return ans