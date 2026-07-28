class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for operation in operations:
            if operation == "+":
                scores.insert(0, scores[0] + scores[1])
            elif operation == "D":
                scores.insert(0, 2 * scores[0])
            elif operation == "C":
                scores.pop(0)
            else:
                scores.insert(0, int(operation))
        return sum(scores)