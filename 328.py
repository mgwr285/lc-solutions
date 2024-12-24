# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds, evens = ListNode(), ListNode()
        p, p1, p2, i = head, odds, evens, 1
        while p:
            print(p.val)
            if i % 2 == 1:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p.next, p = None, p.next
            i += 1
        p1.next = evens.next
        return odds.next
