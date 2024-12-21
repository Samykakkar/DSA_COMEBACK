# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        curr=head
        prev=dummy


        while curr and curr.next:
           next_pair=curr.next.next
           startpt=curr.next

           startpt.next=curr
           curr.next=next_pair
           prev.next=startpt
           prev=curr
           curr=next_pair


        return dummy.next
    
