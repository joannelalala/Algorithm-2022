# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tkinter.tix import ListNoteBook


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a variable, "carry", to deal with the situation: If the sum vertically exceeds 9, the extra digit "carried" into the next column.
        # Start from the left-most column

        dummy = cur = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            cur.next = ListNoteBook(carry % 10) # deal with the extra digit
            cur = cur.next
            carry //= 10 # division reassignment
        return dummy.next

# time: O(max(m, n) + 1), m, n stand for l1 & l2. Needs to loop through max(m, n) + 1, 1 is for "carry".
# space: O(max(m, n) + 1), Need to create an empty list with the size as max(m, n) + 1
# https://leetcode.com/problems/add-two-numbers/


    