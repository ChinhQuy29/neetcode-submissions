class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        operations = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operations:
                first_operand = operand_stack.pop()
                second_operand = operand_stack.pop()
                if token == "+":    
                    operand_stack.append(first_operand + second_operand) 
                elif token == "-":
                    operand_stack.append(second_operand - first_operand) 
                elif token == "*":
                    operand_stack.append(first_operand * second_operand) 
                else:
                    operand_stack.append(int(second_operand / first_operand)) 
            else:
                operand_stack.append(int(token))
        return operand_stack[-1]
                
