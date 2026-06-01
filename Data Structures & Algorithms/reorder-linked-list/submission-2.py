# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        curr = slow.next
        slow.next=None

        prev = None 
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp
            
        curr = prev 
        head1=head
        while curr:
            temp1 = head1.next 
            temp2 = curr.next 
            head1.next = curr
            curr.next = temp1 
            curr = temp2
            head1 = temp1


