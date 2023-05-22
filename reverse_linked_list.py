# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative approach:
        curr=head
        newNext=None
        while curr:
            tempNext=curr.next
            curr.next=newNext
            newNext=curr
            curr=tempNext
        return newNext    
        

        # recursive approach:
        # if head==None or head.next==None:
        #     return head
        # node1=self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return node1
