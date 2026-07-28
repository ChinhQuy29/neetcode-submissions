class Solution:
    def _rec_search(self, l: int, r: int, nums: List[int], target: int) -> bool:
        if l > r:
            return False
        
        m = l + (r - l) // 2
        if nums[m] == target:
            return True
        if nums[m] < target:
            return self._rec_search(m + 1, r, nums, target)
        return self._rec_search(l, m - 1, nums, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for row in matrix:
            temp += row
        return self._rec_search(0, len(temp) - 1, temp, target)