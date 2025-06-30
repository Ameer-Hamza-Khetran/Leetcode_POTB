# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases: if either list is None, return the other list
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        # Create a result node (it will hold the lesser value)
        if list1.val < list2.val:
            result = list1  # Choose list1 if its value is smaller
            result.next = self.mergeTwoLists(list1.next, list2)  # Recursively call with the next node of list1
        else:
            result = list2  # Choose list2 if its value is smaller
            result.next = self.mergeTwoLists(list1, list2.next)  # Recursively call with the next node of list2
        
        return result