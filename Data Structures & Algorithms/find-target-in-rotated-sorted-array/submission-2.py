class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            middle = (l + r) // 2
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle

        pivot = l

        def binary_search(l: int, r: int) -> int:
            while l <= r:
                middle = (l + r) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    r = middle - 1
                else:
                    l = middle + 1
            return -1

        res = binary_search(0, pivot - 1)

        if res != -1:
            return res

        return binary_search(pivot, len(nums) - 1)
                