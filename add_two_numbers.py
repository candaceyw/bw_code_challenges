# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(0)
        res = head
        carry = 0  # to keep track of the remainder

        # add the head of l1 and l2
        # since the numbers are single digit, adding may include a digit to carry over
        # if the number is 9 + 1, we'll drop the 0 in place and then carry the 1 to the             next iteration
        # returned value should be reversed

        # edge cases
        # what is one list is longer than the other?
        # what if one list is empty... won't be in this since we have non-empty lists
        # what if the sum has an extra carry at the end?

        while l1 or l2:
            l1_value = 0
            l2_value = 0

            if l1:
                l1_value = l1.val
            if l2:
                l2_value = l2.val

            curr_sum = l1_value + l2_value + carry

            carry = curr_sum // 10

            res.next = ListNode(curr_sum % 10)

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
            res = res.next

        if carry:
            res.next = ListNode(carry)

        return head.next
