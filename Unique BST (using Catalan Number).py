'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Input: n = 3
Output: 5
'''

def getCatalan(n):
    if n <= 1:
        return 1
        
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]     
                    
    return dp[n]

print(getCatalan(3))
