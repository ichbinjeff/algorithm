class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.merge_k_list(lists, 0, len(lists)-1)

    def merge_k_list(self, lists, start, end):
        if start > end:
            return
        if start == end:
            return lists[start]

        mid = (start + end) / 2
        list1 = self.merge_k_list(lists, start, mid)
        list2 = self.merge_k_list(lists, mid+1, end)
        self.merge_two_list(list1, list2)


    def merge_two_list(self, list1, list2):
        head = ListNode(0)
        curr = head
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
        elif list2:
            curr.next = list2

        return head.next


