# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_all(self):
    	rst = str(self.val)+"->"
    	curr = self.next
    	while curr:
    		rst += str(curr.val)
    		rst += "->"
    		curr = curr.next
    	rst += "null"
    	return rst

def convert_arr_to_list(nums):
	head = ListNode(0)
	curr = head
	for i in range(0, len(nums)):
		curr.next = ListNode(nums[i])
		curr = curr.next
	return head.next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        curr = fast = head

        while fast and fast.next:
        	fast = fast.next.next
        	next = curr.next
        	curr.next = rev
        	rev = curr
        	curr = next

        if fast:
        	curr = curr.next

        while rev and curr:
        	if rev.val != curr.val:
        		return False
        	curr = curr.next
        	rev = rev.next

        return True

head = convert_arr_to_list([1,2,2,1])
print head.print_all()
s = Solution()
print s.isPalindrome(head)
