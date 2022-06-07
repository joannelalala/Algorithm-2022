# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        c1 = ListNode(l1)
        c2 = ListNode(l2)
        
        sentinel = ListNode(0)
        d = ListNode(sentinel)
        total = 0
        
        while c1 or c2:
            total /= 10 
            # '/=' means 'division assignment', for example, a=10, after referencing a/=5, print(a) gets 2
            if c1:
                total += c1.val
                c1 = c1.next
            if c2:
                total += c2.val
                c2 = c2.next
            
            d.next = ListNode(total % 10)
            d = d.next
            
            if total / 10 == 1:
                d.next = ListNode(1)
                
        return sentinel.next
    
    