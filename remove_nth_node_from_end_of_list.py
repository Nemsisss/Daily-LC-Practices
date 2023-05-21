# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        lenOfList=0
#         find the size of the list
        while temp!=None:
            lenOfList+=1
            temp=temp.next
#          if the size of the list is one, then just set head to None
        if lenOfList==1:
            head=None
        else:
#             if limit is zero, then we know we are asked to delete the head
            limit=lenOfList-n
            node=head
            counter=0
#             if the node to be deleted is not the head
            if limit!=0:
#         iterate until we reach the node that is right before the node we want to delete
                while counter!=limit-1:
                    node=node.next
                    counter+=1
#                delete the node
                node.next=node.next.next
#                 if we are trying to delete the head
            else:
                head=head.next
                
        return head

        
