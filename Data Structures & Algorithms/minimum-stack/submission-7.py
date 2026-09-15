class MinStack:
    def __init__(self):
        self.vals = {}
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.vals[val] = self.vals.get(val, 0) + 1

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif (self.min_stack[-1] >= val):
            self.min_stack.append(val)         

    def pop(self) -> None:
        value = self.stack[-1]
        self.stack.pop(-1)
        if (self.min_stack[-1] == value):
            self.min_stack.pop(-1)
    
        self.vals[value] = self.vals.get(value, 1) - 1

    def top(self) -> int:
        return self.stack[-1]
  
    def getMin(self) -> int:
        while (self.vals[self.min_stack[-1]] == 0):
            self.min_stack.pop(-1)

        return self.min_stack[-1]

        
