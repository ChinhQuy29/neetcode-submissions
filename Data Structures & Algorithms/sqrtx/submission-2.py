class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range(x):
            if (i + 1) ** 2 == x:
                return i + 1
            elif i ** 2 > x:
                return i - 1