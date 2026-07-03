class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #fill in min stack if empty or val < top of min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        
    def pop(self) -> None:

        """
        pop from min_stack if the value removed from stack 
        is at the top of min stack
        """
        if self.stack:
            value = self.stack.pop()
            if value == self.getMin():
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return 0

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return 0
