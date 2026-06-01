class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == nullptr || left == right) return head;
        
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* prev = dummy;
        
        // Move prev to the node before position 'left'
        for (int i = 1; i < left; i++) {
            prev = prev->next;
        }
        
        // Start reversing from 'left' to 'right'
        ListNode* curr = prev->next;
        ListNode* next = nullptr;
        
        for (int i = 0; i < right - left; i++) {
            next = curr->next;
            curr->next = next->next;
            next->next = prev->next;
            prev->next = next;
        }
        
        return dummy->next;
    }
};