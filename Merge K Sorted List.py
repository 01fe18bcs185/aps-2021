# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
# Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

a = ListNode(2)
b = ListNode(6)
c = ListNode(8)
l1 = a
a.next = b
b.next = c

d = ListNode(3)
e = ListNode(6)
f = ListNode(7)
l2 = d
d.next = e
e.next = f

g = ListNode(1)
h = ListNode(3)
i = ListNode(4)
l3 = g
g.next = h
h.next = i

from heapq import heappop, heappush

def print_list(node):
    cur = node

    while cur != None:
        print(cur.val,end = ' ')
        cur = cur.next
    print()

def solve(lists):
    pq = []

    for i,root in enumerate(lists):
        heappush(pq,[root.val,i,root]) 

    dummy_head = sorted_tail = ListNode(None)

    while pq:
        dequed = heappop(pq)
        sorted_tail.next = dequed[2]
        sorted_tail = sorted_tail.next

        if dequed[2].next:
            heappush(pq,[dequed[2].next.val, dequed[1], dequed[2].next])
    return dummy_head.next

lists = [l1,l2,l3]
print_list(solve(lists))