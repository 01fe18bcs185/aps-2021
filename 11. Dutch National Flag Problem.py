# Input: [2, 2, 0, 1, 2, 0]
# Output: [0 0 1 2 2 2 ]

a = [2, 2, 0, 1, 2, 0]
left = 0
right = len(a)-1
i = 0

while i <= right:
    if a[i] == 0:
        a[i], a[left] = a[left], a[i]
        i += 1
        left += 1
    elif a[i] == 1:
        i += 1
    else:
        a[i], a[right] = a[right], a[i]
        right -= 1
print(a) 
