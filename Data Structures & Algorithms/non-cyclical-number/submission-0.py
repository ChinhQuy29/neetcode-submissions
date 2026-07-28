class Solution:
    def sum_square_digits(self, num: int) -> int:
        sum = 0
        for digit in str(num):
            sum += int(digit) ** 2
        return sum
    def isHappy(self, n: int) -> bool:
        temp_arr = []
        while True:
            sum_square = self.sum_square_digits(n)
            if sum_square == 1:
                return True
            if sum_square in temp_arr:
                return False
            temp_arr.append(sum_square)
            n = sum_square