class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        lastElement = head
        length = 1
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        k = k % length
        if k == 0:
            return head

        lastElement.next = head

        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        answer = tempNode.next
        tempNode.next = None
        
        return answer
