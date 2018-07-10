class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        place, minDiff = -1, 2*31-1
        for i in range(0, len(words)):
            if words[i] == word1 or words[i] == word2:
                if place != -1 and i != place:
                    print place
                    print i
                    minDiff = min(i-place, minDiff)
                place = i
        return minDiff
    
    # 1
    # def shortestDistance(self, words, word1, word2):
    #     """
    #     :type words: List[str]
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     place = {}
    #     for i in range(0, len(words)):
    #         if words[i] not in place:
    #             place[words[i]] = [i]
    #         else:
    #             place[words[i]].append(i)
        
    #     if word1 not in place or word2 not in place:
    #         return -1
    #     p1 = place[word1]
    #     p2 = place[word2]
    #     minDiff = 2**31-1
    #     for i in p1:
    #         for j in p2:
    #             minDiff = min(abs(i-j), minDiff)
    #     return minDiff

    # 2
    # def shortestDistance(self, words, word1, word2):
    #     """
    #     :type words: List[str]
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     if not words:
    #         return -1
    #     place = {}
    #     p1, p2, minDiff = -1, -1, 2**31-1
    #     for i in range(0, len(words)):
    #         if words[i] == word1:
    #             p1 = i
    #         elif words[i] == word2:
    #             p2 = i
    #         if p1 != -1 and p2 != -1:
    #             minDiff = min(abs(p1-p2), minDiff)
    #     return minDiff

s = Solution()
s.shortestDistance(["a","b","c","d","d"], "a", "d")