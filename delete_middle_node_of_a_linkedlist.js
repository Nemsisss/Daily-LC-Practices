/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
   let n=0;
   let temp=head;
   while(temp!=null)
   {
        n+=1;
        temp=temp.next;
   }
   const middle= Math.floor(n/2);
   let counter=0
   temp=head;
   let prev=null;
   while(counter<=middle)
   {
        if(counter==middle)
        {
            if(prev!=null)
            {
                prev.next=temp.next
            }
            else
            {
                head=null
            }
            temp=null;
            break;
        }
        prev=temp;
        temp=temp.next;
        counter+=1
   }
   return head
    
};