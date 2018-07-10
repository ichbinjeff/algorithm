# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def find_mid(self, head):
   		if not head:
   			return None
   		slow, fast = head, head.next
   		while fast and fast.next:
   			slow = slow.next
   			fast = fast.next.next
   		return slow

    def merge(self, list1, list2):
    	curr = ListNode(0)
        head = curr
    	while list1 and list2:
    		if list1.val <= list2.val:
    			curr.next = list1
    			list1 = list1.next
    		else:
    			curr.next = list2
    			list2 = list2.next
    		curr = curr.next

    	if list1:
    		curr.next = list1

    	if list2:
    		curr.next = list2
    	return head.next
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        mid = self.find_mid(head)
        next = mid.next
        mid.next = None
       	left = self.sortList(head)
       	right = self.sortList(next)
       	return self.merge(left, right)
    
   	