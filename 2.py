# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        p, p1, p2 = dummy, l1, l2
        while p1 or p2 or carry > 0:
            res = carry
            if p1:
                res += p1.val
                p1 = p1.next
            if p2:
                res += p2.val
                p2 = p2.next
            p.next = ListNode(val=res % 10)
            p = p.next
            carry = res // 10
        return dummy.next
