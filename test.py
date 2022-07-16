class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


n2 = ListNode(2)
print(id(n2))
n2.next = None
n2 = 2
print(id(n2))

n1 = ListNode(1)
n1.next = n2
n2 = 1
print(int)
print(id(n2))
print(n1.next.val)
