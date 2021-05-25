'''
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
'''

def prefixSum(A):
    for i in range(1, len(A)):
        A[i] += A[i-1]
    
    return A
 
print(prefixSum([1,2,3,4))
