class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] += 1
        sorted_keys = sorted(frequency_map, key=frequency_map.get, reverse=True)
        return sorted_keys[:k]