# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None):
            return False
        nodes_visited = set([])
        curr = head
        while curr not in nodes_visited:
            nodes_visited.add(curr)
            if (curr.next == None):
                return False
            curr = curr.next
        return True;