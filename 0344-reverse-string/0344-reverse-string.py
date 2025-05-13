class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left, right):
            # Base case: when pointers meet or cross
            if left >= right:
                return
            
            # Swap the elements at the left and right pointers
            s[left], s[right] = s[right], s[left]
            
            # Recursively call with inward pointers
            helper(left + 1, right - 1)
        
        # Call helper with initial pointers at the ends of the list
        helper(0, len(s) - 1)
