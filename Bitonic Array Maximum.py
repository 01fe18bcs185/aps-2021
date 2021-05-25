# Input: [1, 3, 8, 12, 4, 2]
# Output: 12
# Explanation: The maximum number in the input bitonic array is '12'.

def solve(nums):
    n = len(nums)
    start = 0
    end = n-1

    if nums[0] > nums[1]:
        return nums[0]
    if nums[-1] > nums[-2]:
        return nums[-1]

    while start <= end:
        mid = start + (end-start)//2

        middle_num = nums[mid]
        middle_right_num = nums[mid+1]
        middle_left_num = nums[mid-1]

        if middle_left_num < middle_num > middle_right_num:
            return middle_num
        else:
            if middle_left_num < middle_num:
                start = mid+1
            if middle_right_num < middle_num:
                end = mid-1

nums = [1, 3, 8, 12, 4, 2]
print(solve(nums)) 
