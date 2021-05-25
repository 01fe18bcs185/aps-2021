# Input: N=3
# Output: ((())), (()()), (())(), ()(()), ()()()

from collections import deque

class Paranthesis:
    def __init__(self,char,a,b):
        self.char = char
        self.open_count = a
        self.close_count = b

def solve(num):
    queue = deque()
    res = []
    queue.append(Paranthesis('',0,0))

    while queue:
        ps = queue.popleft()

        if ps.open_count == ps.close_count == num:
            res.append(ps.char)
        
        else:
            if ps.open_count < num:
                queue.append(Paranthesis(ps.char + '(', ps.open_count + 1, ps.close_count))
            if ps.open_count > ps.close_count:
                queue.append(Paranthesis(ps.char + ')', ps.open_count, ps.close_count + 1))
    return res

n = 3
print(solve(n))