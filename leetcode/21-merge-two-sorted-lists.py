# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        prev = None
        while l1 or l2:
            if l1 is None:
                node = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                node = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            if head is None:
                head = node
            if prev:
                prev.next = node
            prev = node
        return head
