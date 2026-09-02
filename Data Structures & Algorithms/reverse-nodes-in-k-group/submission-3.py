# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        for i in range(k):
            if not curr:
                return head
            curr = curr.next
        prev = None
        count = 0
        curr = head
        while curr and count < k:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next

            count += 1
        
        head.next = self.reverseKGroup(curr, k)

        return prev
        

