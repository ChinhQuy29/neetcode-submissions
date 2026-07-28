class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            need = target - value
            if need in seen:
                return [seen[need], index]
            else:
                seen[value] = index
        
        