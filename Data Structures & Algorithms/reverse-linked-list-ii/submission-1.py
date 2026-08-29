# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prev = None

        before = None
        start = None
        end = None
        after = None

        index = 1
        while curr:
            if index == left:
                before = prev
                start = curr
            
            if index == right:
                end = curr
                after = curr.next
            
            index += 1
            prev = curr
            curr = curr.next

        curr = head
        index = 1
        while curr:
            if index == left:
                rev = self.reverseList(curr, right - left + 1)
                if before:
                    before.next = end

                start.next = after

                if left > 1:
                    return head
                else:
                    return rev

            index += 1
            curr = curr.next
            
        return after
    
    def reverseList(self, head, length):
        curr = head
        prev = None
        curr_next = None
        latest = None
        index = 1
        while curr and index <= length:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
            index += 1

        return prev