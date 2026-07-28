class MinStack:

    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, val: int) -> None:
        if len(self._stack) == 0:
            self._min.append(val)
        else:
            self._min.insert(0, min(self._min[0], val))
        self._stack.insert(0, val)

    def pop(self) -> None:
        self._stack.pop(0)
        self._min.pop(0)
        

    def top(self) -> int:
        return self._stack[0]
        

    def getMin(self) -> int:
        return self._min[0]
        
