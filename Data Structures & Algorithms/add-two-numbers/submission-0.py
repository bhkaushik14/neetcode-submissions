# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2
        carry = 0

        dummy = ListNode(0)
        curr = dummy

        while curr_l1 or curr_l2 or carry != 0:
            first_val = curr_l1.val if curr_l1 else 0
            second_val = curr_l2.val if curr_l2 else 0

            total = first_val + second_val + carry
            if total < 10:
                curr.next = ListNode(total)
                carry = 0
            else:
                carry = total // 10
                curr.next = ListNode(total % 10)

            curr_l1 = curr_l1.next if curr_l1 else None
            curr_l2 = curr_l2.next if curr_l2 else None

            curr = curr.next

        return dummy.next
