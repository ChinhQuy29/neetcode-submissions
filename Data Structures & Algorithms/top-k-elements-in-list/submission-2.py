class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurencies = {}
        for num in nums:
            if num in occurencies.keys():
                occurencies[num] += 1
            else:
                occurencies[num] = 1
        sorted_dict = dict(sorted(occurencies.items(), key= lambda item: item[1], reverse=True))
        ans = []
        for key, _ in sorted_dict.items():
            ans.append(key)
            if len(ans) == k:
                return ans
            