import heapq
import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rst = []
        freq = collections.defaultdict(int)
        for n in nums:
            freq[n] += 1


        heap = []
        for key, v in freq.iteritems():
            heapq.heappush(heap, (v*(-1), key))

        while k > 0:
            rst.append(heapq.heappop(heap)[1])
            k -= 1

        return rst

s = Solution()
print s.topKFrequent([1,1,1,2,2,2,2,3,3,3,4,5,6], 3)
