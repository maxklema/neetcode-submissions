# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        if (head != None and head.next != None):
            fast = fast.next.next
        else:
            return False

        while (fast != None and fast.next != None):
            if (fast == slow):
                return True
            slow = slow.next
            fast = fast.next.next

        return False