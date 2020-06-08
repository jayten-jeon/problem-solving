# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        while l1.next:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2.next:
            num2.append(str(l2.val))
            l2 = l2.next
        num1.append(str(l1.val))
        num2.append(str(l2.val))
        num1 = int("".join(reversed(num1)))
        num2 = int("".join(reversed(num2)))
        num3 = num1 + num2
        next_node = None
        for num in str(num3):
            node = ListNode(int(num), next_node)
            next_node = node
        return node
