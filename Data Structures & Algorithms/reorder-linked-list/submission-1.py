# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            curr = slow
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            save_next = curr.next
            curr.next = prev
            prev = curr
            curr = save_next
                
        first = head
        second = prev
        while first and second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        

