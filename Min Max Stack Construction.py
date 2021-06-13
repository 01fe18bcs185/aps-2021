# Write a MinMaxStack class for a Min Max Stack. The class should support:

# Pushing and popping values on and off the stack.
# Peeking at the value at the top of the stack.
# Getting both the minimum and the maximum values in the stack at any given point in time.

class MinMaxStack:
    def __init__(self):
        self.min_max_stack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.min_max_stack.pop()
        return self.stack.pop()

    def push(self, number):
        new_min_max = {"min": number, "max": number}
        if len(self.min_max_stack):
            last_min_max = self.min_max_stack[len(self.min_max_stack) - 1]
            new_min_max["min"] = min(last_min_max["min"], number)
            new_min_max["max"] = max(last_min_max["max"], number)
        self.min_max_stack.append(new_min_max)
        self.stack.append(number)

    def getMin(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]["min"]

    def getMax(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]["max"]

