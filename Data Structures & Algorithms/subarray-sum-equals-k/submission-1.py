from typing import List
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = collections.defaultdict(int)

        prefix_sums[0] = 1

        count = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            required_prefix = current_sum - k
            if required_prefix in prefix_sums:
                count += prefix_sums[required_prefix]
            
            prefix_sums[current_sum] += 1
        return count