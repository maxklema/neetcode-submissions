# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_visited = set([])
        curr = head
        while curr not in nodes_visited:
            if (curr == None or curr.next == None):
                return False
            nodes_visited.add(curr)
            curr = curr.next
        return True;