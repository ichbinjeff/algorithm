class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
        else:
            return None

        slow = head
        while slow:
            if slow == fast:
                return slow
            fast = fast.next
            slow = slow.next
        return None


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


s = Solution()
one = ListNode(1)
two = ListNode(2)
one.next = two
two.next = one
s.detectCycle(one)