# Input: {1, 2, 3, 7}, S=6
# Output: True
# The given set has a subset whose sum is '6': {1, 2, 3}

nums = [1, 2, 3, 7]
s = 6

def solve(nums,s):
    n = len(nums)

    dp = [[False for _ in range(s+1)] for _ in range(n)]

    for i in range(0,n):
        dp[i][0] =  True
    
    for j  in range(s+1):
        dp[0][j] = (nums[0] == j)
    
    for i in range(1,n):
        for j in range(1,s+1):
            if dp[i-1][j]:
                dp[i][j] = True
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
    
    return dp[n-1][s]


print(solve(nums,s)) 