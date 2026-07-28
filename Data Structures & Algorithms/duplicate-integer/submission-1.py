class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = []
        for num in nums:
            if num in num_set:
                return True
            num_set.append(num)
        return False