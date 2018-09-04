# coding=utf-8
# 1.visited 很重要，记录那些被访问过
# 2.visited 应该是hashset，这样可以直接判断是否被访问过
# 3.要考虑mid为3的情况，取一个zhi作为mid，其余继续参与permutation
class Solution(object):
    def generatePalindromes(self, s):
        count = {character: 0 for character in s}
        for character in s:
            count[character] += 1
        letters, mid, first = "", "", True
        mid = [k for k, v in count.iteritems() if v%2 == 1]
        if len(mid) > 0:
            return []
        else:
            mid = mid[0]
            count[mid] -= 1

        for k,v in count.iteritems():
            letters += k*(v/2)

        rst, level, visited = [], [], set()
        # rst is letters + mid + reverse(letters)
        self.permutate(rst, level, visited, letters, mid)
        return rst

    def permutate(self, rst, level, visited, letters, mid):
        if len(level) == len(letters):
            rst.append("".join(level)+mid+"".join(reversed(level)))
            return

        for i in range(len(letters)):
            if i not in visited:
                if i >= 1 and (letters[i-1] == letters[i] and i-1 not in visited):
                    continue

                level.append(letters[i])
                visited.add(i)
                self.permutate(rst, level, visited, letters, mid)
                visited.discard(i)
                level.pop()

    # brutal force dfs
    # def generatePalindromes(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #     rst = []
    #     level = []
    #     visited = set()
    #     self.dfs(rst, level, visited, sorted(s))
    #     return rst
    #
    # def dfs(self, rst, level, visited, s):
    #     if len(level) == len(s) and self.is_palindrome(level):
    #         rst.append("".join(level))
    #         return
    #
    #     for i in range(len(s)):
    #         if i in visited:
    #             continue
    #         if i > 0 and s[i - 1] == s[i] and i - 1 not in visited:
    #             continue
    #         visited.add(i)
    #         level.append(s[i])
    #         self.dfs(rst, level, visited, s)
    #         level.pop()
    #         visited.discard(i)
    #
    # def is_palindrome(self, charlist):
    #     start, end = 0, len(charlist) - 1
    #     while start < end:
    #         if charlist[start] != charlist[end]:
    #             return False
    #         start += 1
    #         end -= 1
    #     return True
    #
    #
