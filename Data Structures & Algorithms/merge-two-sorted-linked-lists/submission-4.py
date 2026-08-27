# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None):
            return list2
        elif (list2 == None):
            return list1
        
        head = ListNode()
        list1_curr = list1
        list2_curr = list2
        if (list1.val > list2.val):
            head.next = list2_curr
            list2_curr = list2_curr.next
        else:
            head.next = list1_curr
            list1_curr = list1_curr.next
        curr = head.next

        while (list1_curr != None and list2_curr != None):
            if (list1_curr.val > list2_curr.val):
                curr.next = list2_curr
                list2_curr = list2_curr.next
            else:
                curr.next = list1_curr
                list1_curr = list1_curr.next
            curr = curr.next

        if (list1_curr != None):
            curr.next = list1_curr
        elif (list2_curr != None):
            curr.next = list2_curr

        return head.next



        