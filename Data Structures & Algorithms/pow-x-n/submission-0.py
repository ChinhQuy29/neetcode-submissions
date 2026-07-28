class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        elif n > 0:
            return x * self.myPow(x, n - 1)
        else:
            return 1/float(x) * self.myPow(1/float(x), abs(n) - 1)