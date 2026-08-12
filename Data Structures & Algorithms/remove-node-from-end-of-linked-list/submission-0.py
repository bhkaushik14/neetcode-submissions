# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head

        while current:            
            count += 1
            current = current.next

        n = count - n

        if n == 0 and head:
            return head.next

        count = 0
        current = head

        while current and current.next:
            if count == n - 1:
                current.next = current.next.next
            else:
                current = current.next

            count += 1

        return head