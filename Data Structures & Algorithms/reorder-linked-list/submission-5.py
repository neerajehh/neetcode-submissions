# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head 
        slow = head 
        current = head 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        new = slow.next
        slow.next = None 
        prev = None 
        curr = new 
        while curr: 
            temp = curr.next  
            curr.next = prev
            prev = curr 
            curr = temp 
       
        new1 = prev 
        while new1: 
            temp1 = new1.next
            temp2 = current.next
            current.next = new1 
            new1.next = temp2
            current = temp2
            new1 = temp1
