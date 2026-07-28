class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occurrences = {}
        for num in nums:
            if num not in occurrences.keys():
                occurrences[num] = 1
            else:
                occurrences[num] += 1
        res = []
        for item in occurrences.items():
            if item[1] > len(nums) // 3:
                res.append(item[0])
        return res