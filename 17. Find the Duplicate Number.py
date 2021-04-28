# Input: [1, 4, 4, 3, 2]
# Output: 4

nums = [1, 4, 4, 3, 2]
i = 0
n = len(nums)

while i < n:
    j = nums[i]-1
    if nums[i]!=nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
    else:
        i += 1
        
print(nums[-1]) 
