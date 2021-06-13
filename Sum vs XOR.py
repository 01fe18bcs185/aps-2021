# Given an integer n, count the number of patterns with n+x = n^x, where 0<=x<=n

def solve(n):
    return 2**(bin(n)[1:].count('0'))

print(solve(n))
