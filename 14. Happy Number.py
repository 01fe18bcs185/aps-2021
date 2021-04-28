# Input: 23   
# Output: true (23 is a happy number)  
# Explanations: Here are the steps to find out that 23 is a happy number:
n = 24

def cal(n):
    res = sum(int(x)**2 for x in str(n))
    return res


slow = fast = n

while fast:
    slow = cal(slow)
    fast = cal(cal(fast))

    if slow == fast:  #cycle detected.
        break
print(slow == 1)

