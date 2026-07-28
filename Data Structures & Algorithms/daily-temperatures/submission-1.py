class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [(0, temperatures[0])]
        for i in range(1, len(temperatures)):
            while (len(stack) > 0) and (temperatures[i] > stack[0][1]):
                result[stack[0][0]] = i - stack[0][0]
                stack.pop(0)
            stack.insert(0, (i, temperatures[i]))
        return result
