class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.place = {}
        for i in range(0, len(words)):
            if words[i] not in self.place:
                self.place[words[i]] = [i]
            else:
                self.place[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        minDiff = 2**31-1
        wl1 = self.place[word1]
        wl2 = self.place[word2]
        
        index1, index2 = 0, 0
        while index1 < len(wl1) and index2 < len(wl2):
            minDiff = min(minDiff, abs(wl1[index1] - wl2[index2]))
            if wl1[index1] < wl2[index2]:
                index1 += 1
            else:
                index2 += 1
        print index1
        print index2
        return minDiff

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)