class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateDict= {}
        for i in range(len(nums)):
            if nums[i] in duplicateDict.keys():
                return True
            else:
                duplicateDict.update({nums[i]: 1})
        return False
    
        