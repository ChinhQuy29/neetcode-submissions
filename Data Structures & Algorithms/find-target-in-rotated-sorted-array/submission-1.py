class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = 0
        while l <= r:
            if nums[l] < nums[r]:
                if nums[pivot] > nums[l]:
                    pivot = l
                break
            
            middle = (r + l) // 2
            if nums[pivot] > nums[middle]:
                pivot = middle
            
            if nums[middle] >= nums[l]:
                l = middle + 1
            else:
                r = middle - 1

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
        
        first = binary_search(0, pivot - 1)
        second = binary_search(pivot, len(nums) - 1)

        if first == -1 and second == -1:
            return -1
        
        return abs(first * second)
                