class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def lowerbound(arr: List[int], x: int):
            l, r = 0, len(arr) - 1
            res = len(arr)

            while l <= r:
                m = (l + r) // 2
                if arr[m] < x:
                    res = m
                    l = m + 1
                else:
                    r = m - 1
            
            return res
        
        res = []

        l = lowerbound(arr, x)

        if l == len(arr):
            return arr[:k]

        if l == len(arr) - 1:
            return arr[-k:]
            
        r = l + 1
        while len(res) < k:
            if r > len(arr) - 1:
                res.append(arr[l])
                l -= 1
                continue
            
            if l < 0:
                res.append(arr[r])
                r += 1
                continue
                
            if abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        
        return sorted(res)

        
        