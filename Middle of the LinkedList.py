#Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
#Output: 3

class Node:
    def __init__(self,data):
        self.val = data
        self.next= None
        

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c

head = a

slow = fast = head

while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
print(slow.val)
