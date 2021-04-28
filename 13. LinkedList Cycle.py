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
#Cycle detection
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        print("Cycle detected")
        break
 
