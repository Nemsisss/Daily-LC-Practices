# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # temps=[]
        # tempHead=head
        # while tempHead:
        #     if tempHead in temps:
        #         return True
        #     temps.append(tempHead)
        #     tempHead=tempHead.next
        # return False
        
#         using dictionary
        temps=dict()
        tempHead=head
        while tempHead:
            if tempHead in temps :
                return True
            temps[tempHead]=1
            tempHead=tempHead.next
        return False
        
