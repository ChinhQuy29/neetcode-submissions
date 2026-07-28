class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            num = i
            count = 0
            while num:
                if num % 2:
                    count += 1
                num = num // 2
            res.append(count)
        return res