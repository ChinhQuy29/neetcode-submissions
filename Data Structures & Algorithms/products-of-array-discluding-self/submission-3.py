class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        if zero_count >= 2:
            return [0] * len(nums)
        
        result = []
        if zero_count == 1:
            for num in nums:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            return result
        
        for num in nums:
            result.append(int(product / num))
        
        return result