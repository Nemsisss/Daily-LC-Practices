# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lenOfl1=0
        lenOfl2=0
        tempNode = l1
        tempArr1=[]
        tempArr2=[]
        
        # to calculate length of l1
        while tempNode is not None:
            lenOfl1+=1
            tempArr1.append(tempNode.val)
            tempNode = tempNode.next
        
        # to calculate length of l2
        tempNode=l2
        while tempNode is not None:
            lenOfl2+=1
            tempArr2.append(tempNode.val)
            tempNode = tempNode.next

        # pad the arrays if linkedlists don't have the same length
        if lenOfl1 > lenOfl2:
            while len(tempArr2)<len(tempArr1):
                tempArr2.append(0)
        elif lenOfl1 < lenOfl2:
            while len(tempArr1)<len(tempArr2):
                tempArr1.append(0)
        
        carry=0
        startNode = l1 if lenOfl1 > lenOfl2 else l2
        toRetNode= startNode
        # update the bigger linkedlist to hold the summed values
        for i in range(len(tempArr1)):
            sum = tempArr1[i]+tempArr2[i]+carry
            if sum>=10:
                carry=1
                sum=sum%10
            else:
                carry=0
            startNode.val = sum
            if startNode.next is not None:
                startNode=startNode.next
        
        if carry==1:
            startNode.next = ListNode(1,None)

        return toRetNode
            
