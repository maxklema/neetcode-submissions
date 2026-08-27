class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        l1, l2 = list1, list2
        dummy = head

        while (l1 != None and l2 != None):
            if (l1.val > l2.val):
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next

        if (l1 == None):
            head.next = l2
        elif (l2 == None):
            head.next = l1

        return dummy.next

