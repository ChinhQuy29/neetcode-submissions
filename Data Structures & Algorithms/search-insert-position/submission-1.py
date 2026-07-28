class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = len(nums)
        while l <= r:
            middle = (r + l) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                res = middle
                r = middle - 1
            else:
                l = middle + 1
        return res
                
        