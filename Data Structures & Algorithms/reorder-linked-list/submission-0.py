# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow=head.next,head
        while fast and fast.next :
            slow = slow.next
            fast= fast.next.next

        secound = slow.next
        slow.next=None
        prev=None

        while secound:
            temp = secound.next
            secound.next = prev
            prev=secound
            secound = temp
        
        first,secound=head,prev
        while secound:
            tmp1,tmp2=first.next,secound.next
            first.next=secound
            secound.next=tmp1
            first=tmp1
            secound= tmp2

            
        
        