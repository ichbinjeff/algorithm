# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        char_set = ['A', 'C', 'T', 'G']
        span = -1
        queue = [start]
        while len(queue) > 0:
            size = len(queue)
            span += 1
            for s in range(size):
                top = queue.pop(0)
                for i in range(0, len(top)):
                    for c in char_set:
                        if c == top[i]:
                            continue
                        new_word = top[:i]+str(c)+top[i+1:]
                        if new_word in bank:
                            if new_word == end:
                                return span+1
                            queue.append(new_word)
        return -1

