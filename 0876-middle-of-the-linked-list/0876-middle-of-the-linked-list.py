# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenLinkedList = 0
        curr = head
        while curr:
            curr = curr.next
            lenLinkedList += 1
        mid = lenLinkedList // 2
        print(mid)
        for i in range(mid+1):
            if i == (mid):
                return head
            head = head.next