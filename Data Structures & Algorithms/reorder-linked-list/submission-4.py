# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head 
        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 
        mid = slow.next # partion into 2 linked lists 
        slow.next = None 
        # reversing second portion of linked list 
        prev = None 
        curr = mid 
        while curr:
            temp = curr.next  
            curr.next = prev 
            prev = curr 
            curr = temp 
        first =  head  # new head of reversed linked list 
        second = prev 
        while second : 
         temp1 = first.next
         temp2 = second.next
         first.next = second
         second.next = temp1 
         first = temp1 
         second = temp2 



