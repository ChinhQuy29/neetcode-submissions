class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [float("inf")] * len(nums)
        memo[0] = 0
        for i in range(len(nums)):
            for step in range(1, nums[i] + 1):
                if i + step >= len(nums):
                    break
                memo[i + step] = min(memo[i] + 1, memo[i + step])
        
        return memo[-1]