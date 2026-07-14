class Solution(object):
    def sortList(self, head):

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        values.sort()
        curr = head
        for val in values:
            curr.val = val
            curr = curr.next
        
        return head
