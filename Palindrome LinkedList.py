# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        curr, prev = slow, None
        while(curr):
            currnext = curr.next
            curr.next = prev
            prev = curra
            curr = currnext
        
        end = prev
        left, right = head, end

        while(right):
            if(left.val != right.val):
                return False
            right = right.next
            left = left.next
        return True
