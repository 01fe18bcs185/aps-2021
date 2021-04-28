# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

a = [1, 2, 3, 4, 6]
target = 6

left = 0
right = len(a)-1

while left < right:
    cur_target = a[left] + a[right]
    if cur_target == target:
        print(left,right)
        break
    elif cur_target < target:
        left += 1
    else:
        right -= 1 
