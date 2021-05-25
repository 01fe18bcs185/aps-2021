class Node:
    def __init__(self, value):
        self.next = None
        self.val = value

a = Node(2)
b = Node(4)
c = Node(6)
d = Node(8)
e = Node(10)

a.next = b
b.next = c
c.next = d
d.next = e

head = a

###################################################
#Reversing a LL

def reverse(head):
    prev = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

reversed_head = reverse(head)
print_list(reversed_head)
