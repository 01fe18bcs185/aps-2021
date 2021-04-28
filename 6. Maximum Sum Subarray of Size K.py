# Input: nums = [2, 1, 5, 1, 3, 2], k=3 
# Output: 9 
# Explanation: Subarray with maximum sum is [5, 1, 3].

res = 0
window_sum = sum(nums[:k])
res = window_sum

for i in range(k, len(nums)):
	window_sum -= nums[i-k]
	window_sum += nums[i]
	res = max(res, window_sum)

print(res) 
