# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 0-1-2-3-4-5

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            last = curr.next.next.next
            next = curr.next.next

            curr.next.next.next = curr.next
            curr.next = next
            curr.next.next.next = last

            curr = curr.next.next

        return dummy.next

    # 1-2-3-4-5
    # 1-2-4-3-5



    def swapPairs(self, head):
        if not head.next or not head.next.next:
            return head
        next = head.next.next
        head.next.next = head
        head.next = self.swapPairs(next)
        head = head.next
        return head
