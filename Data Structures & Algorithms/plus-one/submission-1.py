class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            s = carry + digits[i]
            digits[i] = s % 10
            carry = s // 10
        if carry == 1:
            digits.insert(0, 1)
        return digits