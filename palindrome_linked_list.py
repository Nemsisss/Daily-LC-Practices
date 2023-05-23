# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         O(n)space and time approach#1
        # queue=[]
        # temp=head
        # while temp:
        #     queue.append(temp.val)
        #     temp=temp.next
        # while len(queue)>1:
        #     if queue.pop(0) != queue.pop(-1):
        #         return False
        # return True
  #         O(n)space and time approach#2      
#         result = []
#         curr = head
#         while curr:
#             result.append(curr.val)
#             curr = curr.next
        
#         return result == result[::-1]
        
        #O(n) time and O(1) space
        lenOfList=0
        tempHead= head
        while tempHead:
            lenOfList+=1
            tempHead=tempHead.next
        tempHead=head
        counter=0
#         find the head of the second half of the list
        while counter< (math.floor(lenOfList/2)):
            tempHead=tempHead.next
            counter+=1
#         now tempHead holds the head of the second half of the list
#         reverse the second half of the list
        prev=None
        while tempHead:
            tempNext=tempHead.next
            tempHead.next=prev
            prev=tempHead
            tempHead=tempNext
        tempHead=head
        while tempHead and prev:
            if tempHead.val != prev.val:
                return False
            tempHead=tempHead.next
            prev=prev.next
        return True
        
            
            
        
