# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.

a = [-3, 0, 1, 2, -1, 1, -2]
a.sort()

for i in range(len(a)-2):
    target = 30 - a[i]
    left = i+1
    right = len(a)-1

    while left < right:
        cur_sum = a[left]+a[right]
        if  cur_sum == target:
            print(a[i],a[left],a[right])
            left += 1
            right -= 1
        elif cur_sum < target:
            left += 1
        else:
            right -= 1 
