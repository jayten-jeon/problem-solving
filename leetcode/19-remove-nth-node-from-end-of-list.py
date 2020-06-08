# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        cache = []
        node = head
        while node:
            cache.append(node)
            node = node.next
            size += 1
        if size == 1:
            return None
        target = size - n
        if target == 0:
            head = cache[1]
        else:
            cache[target - 1].next = cache[target].next
        print(size, cache)
        return head
