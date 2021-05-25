# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
        
    dp = [nums[0], max(nums[0], nums[1])]
    res = max(dp)
    
    for i in range(2, len(nums)):
        dp.append(max(dp[i-1], nums[i] + dp[i-2]))
        res = max(res, dp[i])
    
    return res

print(rob([1,2,3,1]))