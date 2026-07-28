class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(i, len(nums)):
                    if nums[i] != nums[j]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
        res = 0
        for num in nums:
            if num != val:
                res += 1
            else:
                break
        return res