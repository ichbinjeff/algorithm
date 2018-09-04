class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cache = {}
        return self._minDistance(word1, 0, word2, 0, cache)

    def _minDistance(self, word1, start1, word2, start2, cache):
        if (start1, start1) in cache:
            return cache(start1, start2)

        if start1 == len(word1):
            return len(word2)-start2
        if start2 == len(word2):
            return len(word1)-start1
        if word1[start1] == word2[start2]:
            curr_min = min(self._minDistance(word1, start1, word2, start2+1, cache)+1, min(self._minDistance(word1, start1+1, word2, start2+1, cache), self._minDistance(word1, start1+1, word2, start2, cache)+1))
        else:
            curr_min = min(self._minDistance(word1, start1, word2, start2+1, cache)+1,min(self._minDistance(word1, start1+1, word2, start2+1, cache)+1, self._minDistance(word1, start1+1, word2, start2, cache)+1))
        cache[(start1, start2)] = curr_min
        return curr_min
