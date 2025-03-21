# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None

        while len(lists)>1:
            resultList=[]

           
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if(i+1)<len(lists) else  None
                resultList.append(self.mergelist(l1,l2))
            lists=resultList
        return lists[0]

    def mergelist(self,l1,l2):
        dummy=ListNode()
        curr=dummy

        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        
        if l1:
            curr.next=l1
        
        if l2:
            curr.next=l2
        # while l2:
        #     curr.netx=l2
        #     l2=l2.next
        
        return dummy.next
        