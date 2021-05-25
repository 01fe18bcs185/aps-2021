'''
Given an array nums with n integers, find if it could become non-decreasing by modifying at most one element.

Input: nums = [4,2,3]
Output: true
Explanation: Modify the first 4 to 1 to get a non-decreasing array.
'''

def isNonDecreasing(A):
        one = A[:]
        two = A[:]
        
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                one[i] = A[i+1]
                two[i+1] = A[i]
                break
        
        return one == sorted(one) or two == sorted(two)
        
print(isNonDecreasing([4,2,3]))
