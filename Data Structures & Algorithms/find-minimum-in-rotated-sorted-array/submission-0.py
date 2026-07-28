class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break
            
            middle = (left + right) // 2
            res = min(nums[middle], res)
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        return res