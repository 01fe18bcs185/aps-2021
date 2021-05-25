# Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
# Output: [4, 6]

a = [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
all_xor = 0

for i in a:
    all_xor ^= i

right_most_set_bit = 1

while (all_xor & right_most_set_bit) == 0:
    right_most_set_bit = right_most_set_bit << 1

num1 = num2 = 0

for num in a:
    if (num & right_most_set_bit) !=0:
        num1 ^= num
    else:
        num2 ^= num

print(num1,num2)