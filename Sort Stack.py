# Write a function that takes in an array of integers representing a stack, recursively sorts the stack in place (i.e., doesn't create a brand new array), and returns it.

def sortStack(stack):
    if not stack:
		return stack
	
	top = stack.pop()
	sortStack(stack)
	insert(stack, top)
	
	return stack

def insert(stack, value):
	if len(stack) == 0 or stack[len(stack)-1] <= value:
		stack.append(value)
		return 
	
	top = stack.pop()
	insert(stack, value)
	
	stack.append(top)
