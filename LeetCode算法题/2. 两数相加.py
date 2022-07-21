# https://leetcode.cn/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        cur = ans
        while l1 or l2:
            if l1 and l2:
                cur.val += l1.val + l2.val
            if l1 and not l2:
                cur.val += l1.val
            if l2 and not l1:
                cur.val += l2.val
            if cur.val > 9:
                cur.val -= 10
                cur.next = ListNode(1)
            else:
                cur.next = ListNode(0)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if not l1 and not l2:
                if cur.next.val == 0:
                    cur.next = None
                    return ans
                else:
                    return ans
            cur = cur.next
