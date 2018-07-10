# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        sorted_list = ListNode(0)
        while head:
            next = head.next
            curr = sorted_list
            while curr.next and curr.next.val <= head.val:
                curr = curr.next
            head.next = curr.next
            curr.next = head
            head = next
        return sorted_list.next
    
s = Solution()
four = ListNode(4)
two = ListNode(2)
one = ListNode(1)
three = ListNode(3)

four.next = two
two.next = one
one.next = three
print s.insertionSortList(four).
