class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operations = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operations:
                operands.append(int(token))
            else:
                second = operands.pop()
                first = operands.pop()
                if token == "+":
                    operands.append(first + second)
                elif token == "-":
                    operands.append(first - second)
                elif token == "*":
                    operands.append(first * second)
                else:
                    operands.append(int(first / second))
        return operands[0]