# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # create dummy variables for tmp_result, and cur_result
        # and set "carry" as 0 for storing tens digits when the sum exceeds 9

        carry = 0
        head_result = tmp_result = ListNode(0)

        # While loop until there are neither nodes nor carries left
        while (l1 != None or l2 != None or carry > 0):
            # Store the values of the LinkedList to variables, and set 0 if no more nodes needs to loop through
            x = (l1.val if l1 else 0)
            y = (l2.val if l2 else 0)

            # Calculate the sum
            sum_res = x + y + carry

            # Make the tens of the sum to be carry
            carry = carry // 10

            # Store the units of the sum to be the result's next node
            tmp_result.next = ListNode(sum_res % 10)

            # Traverse to the next result's node
            tmp_result = tmp_result.next

            # Traverse to the next nodes in the LinkedLists, a.k.a, l1 and l2
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        # Make sure no carries are left
        if carry > 0: # meaning there are carries left, storing it in tmp_result
            tmp_result.next = ListNode(carry)
        # Set the head of the result to skip zero initialization, if there is something in the next node
        if head_result.next != None:
            head_result = head_result.next

        return head_result

    # https://stackoverflow.com/questions/54794410/leetcode-add-twosum-the-listnode-is-not-defined-error

    







