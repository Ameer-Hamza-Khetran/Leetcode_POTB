# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the midpoint using fast and slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the first half of the list
        prev = None
        while head != slow:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
    
        # Step 3: Compare the reversed first half with the second half
        if fast:  # If the list has an odd number of elements, fast will not be None
            slow = slow.next  # Skip the middle element for odd-length lists

        while prev:  # prev points to the reversed first half
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        
        return True