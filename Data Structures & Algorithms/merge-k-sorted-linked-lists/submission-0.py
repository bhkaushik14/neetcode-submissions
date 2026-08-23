# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l1 = []
        if not lists:
            return None

        for curr in lists:
            while curr:
                l1.append(curr.val)
                curr = curr.next
        
        l1.sort()

        head = ListNode(0)
        newl = head

        for num in l1:
            newl.next = ListNode(num)
            newl = newl.next
        
        return head.next