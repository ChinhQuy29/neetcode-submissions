class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                if sorted_nums[left] + sorted_nums[right] + sorted_nums[i] > 0:
                    right -= 1
                elif sorted_nums[left] + sorted_nums[right] + sorted_nums[i] < 0:
                    left += 1
                else:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    right -= 1
                    left += 1

                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1

        return res
