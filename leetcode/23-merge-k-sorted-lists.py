# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        prev = None
        while any(lists):
            lists = [l for l in lists if l]
            min_val = min([node.val for node in lists])
            for i in range(len(lists)):
                if lists[i].val == min_val:
                    lists[i] = lists[i].next
                    break
            min_node = ListNode(min_val)
            if  prev is not None:
                prev.next = min_node
            if head is None:
                head = min_node
            prev = min_node
        return head
