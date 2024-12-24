# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort(head):
            if not head or not head.next:
                return head
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            p1, p2 = head, slow.next
            slow.next = None
            p1 = sort(p1)
            p2 = sort(p2)
            dummy = ListNode()
            p = dummy
            while p1 or p2:
                if p1 and p2:
                    if p1.val <= p2.val:
                        p.next = p1
                        p1 = p1.next
                    else:
                        p.next = p2
                        p2 = p2.next
                elif p1:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            return dummy.next

        return sort(head)
