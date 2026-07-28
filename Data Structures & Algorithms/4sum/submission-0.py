class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return None
        def threeSum(nums, n):
            sorted_nums = sorted(nums)
            triplets = []
            for i in range(len(nums) - 2):
                j, k= i + 1, len(sorted_nums) - 1
                while j < k:
                    if sorted_nums[j] + sorted_nums[k] + sorted_nums[i] < n:
                        j += 1
                    elif sorted_nums[j] + sorted_nums[k] + sorted_nums[i] > n:
                        k -= 1
                    else:
                        triplets.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                        j += 1
                        k -= 1
                        while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                            j += 1
                        while j < k and sorted_nums[k] == sorted_nums[k + 1]:
                            k -= 1
            return triplets
        quadruplets = []
        for i in range(len(nums) - 3):
            triplets = threeSum(nums[i + 1:], target - nums[i])
            if triplets:
                for triplet in triplets:
                    triplet.append(nums[i])
                    if sorted(triplet) not in quadruplets:
                        quadruplets.append(sorted(triplet))
        return quadruplets
                    

        