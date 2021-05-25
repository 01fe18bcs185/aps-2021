# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted


nums = [1, 2, 5, 3, 7, 10, 9, 12]

l = 0
r = len(nums) - 1

for i in range(1, len(nums)):
	if nums[i] < nums[i - 1]:
		l = i
		break

for i in range(len(nums)-2, -1, -1):
	if nums[i] > nums[i + 1]:
		r = i
		break

left = nums[:l]
substr = nums[l : r + 1]
right = nums[r + 1:]

m = min(substr)
M = max(substr)
start = l 
end = r 

i = l - 1
while i >= 0 and nums[i] > m:
	i -= 1
start = i + 1 

i = r + 1
while i < len(nums) and nums[i] < M:
	i += 1
stop = i - 1 

substr = nums[start : stop + 1]
print(substr)

