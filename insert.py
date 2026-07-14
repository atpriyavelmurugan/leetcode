class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        d= ListNode(0)
        current = head
        
        while current:
            next_node = current.next
            prev = d
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            current.next = prev.next
            prev.next = current
            current = next_node
            
        return d.next
