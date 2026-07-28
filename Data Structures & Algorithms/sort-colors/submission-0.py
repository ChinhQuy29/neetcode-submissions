import collections
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        occurrences = collections.defaultdict(int)
        for num in nums:
            occurrences[num] += 1
        for i in range(len(nums)):
            if occurrences[0]:
                nums[i] = 0
                occurrences[0] -= 1
            elif occurrences[1]:
                nums[i] = 1
                occurrences[1] -= 1
            else:
                nums[i] = 2
                occurrences[2] -= 1
        return nums