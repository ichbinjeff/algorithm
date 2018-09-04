"foo"
"food"
"fool"
"foot"

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return self._longestCommonPrefix(0, len(strs)-1, strs)

    def _longestCommonPrefix(self, start, end, strs):
        if start > end:
            return ""
        if start == end:
            return strs[start]
        mid = (start + end) / 2
        left = self._longestCommonPrefix(start, mid)
        right = self._longestCommonPrefix(mid+1, end)
        return self.find_common_prefix(left, right)

    def find_common_prefix(self, left, right):
        for i in range(0, left):
            if i >= len(right) or right[i] != left[i]:
                return left[:i]
        return left



 def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        benchmark = strs[0]
        for i in range(0, len(benchmark)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != benchmark[i]:
                    return benchmark[0:i]

        return benchmark