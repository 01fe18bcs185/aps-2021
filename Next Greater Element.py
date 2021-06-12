# Write a function that takes in an array of integers and returns a new array containing, at each index, the next element in the input array that's greater than the element at that index in the input array
# If there's no such next greater element for a particular index, the value at that index in the output array should be -1.
# Additionally, your function should treat the input array as a circular array.

# Example
# Input: [2, 5, -3, -4, 6, 7, 2]
# Output: [5, 6, 6, 6, 7, -1, 5]

def nextGreaterElement(A):
	n = len(A)
	
    res = [-1] * n
	stack = []
	
	for i in range(2*n):
		i = i % n
		
		while stack and A[stack[-1]] < A[i]:
			top = stack.pop()
			res[top] = A[i]
		
		stack.append(i)
	
	return res
		
