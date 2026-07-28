class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        dummy = ListNode(0, head)
        prev = dummy
    
        while prev.next and prev.next.next:
       
            if prev.next.val == prev.next.next.val:
                duplicate_val = prev.next.val
           
                while prev.next and prev.next.val == duplicate_val:
                    prev.next = prev.next.next
            else:
                prev = prev.next
            
        return dummy.next

