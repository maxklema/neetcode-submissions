# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head
        while (curr != None):
            nx = curr.next
            curr.next = None
            nodes.append(curr)
            curr = nx
        
        for i in range(len(nodes) // 2):
            listNode = nodes[i]
            listNode.next = nodes[-1-i]
            
            if ((len(nodes)-i-1) > i+1):
                nex = listNode.next
                nex.next = nodes[i+1]
            else:
                break

