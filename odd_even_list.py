# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddH = ListNode(0)
        evenH = ListNode(0)
        currOdd, currEven = oddH, evenH
        
        count = 0
        while head:
            count += 1
            next = head.next
            head.next = None
            if count % 2 == 1:
                currOdd.next = head
                currOdd = currOdd.next
            else:
                currEven.next = head
                currEven = currEven.next
            head = next
        
        currOdd.next = evenH.next
        return oddH.next

    def oddEvenList(self, head):
        if not head:
            return head

        odd, even = head, head.next
        evenH = even
        while head:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            head = head.next
        odd.next = evenH
        return head







