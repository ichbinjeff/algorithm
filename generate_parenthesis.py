class Solution(object):
    # brutal force 0, 3, -1
    # def generateParenthesis(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[str]
    #     """
    #     if n <= 0:
    #         return ""
    #
    #     rst = []
    #     self._generateParenthesis(rst, n, "")
    #     return rst
    #
    # def _generateParenthesis(self, rst, level, n, pre):
    #     if n == 0:
    #         rst.append("".join(level))
    #         return
    #
    #     addon = "()"
    #     if not pre:
    #         self._generateParenthesis(rst, n-1, addon)
    #     deDup = set()
    #     for i in range(len(pre)):
    #         curr = str(pre[:i]+addon+pre[i:])
    #         if curr in deDup:
    #             continue
    #         deDup.add(curr)
    #         self._generateParenthesis(rst, n-1, curr)
    #
    #


    def generateParenthesis(self, n):
        rst = []
        self._generateParenthesis(rst, "", n, 0)
        return rst

    def _generateParenthesis(self, rst, curr, n, r):
        print "curr: {0}".format(curr)
        if n == 0 and r == 0:
            rst.append(curr)
            return
        if n > 0:
            self._generateParenthesis(rst, curr+"(", n-1, r+1)
        if r > 0:
            self._generateParenthesis(rst, curr+")", n, r-1)


s = Solution()
s.generateParenthesis(2)

# recursion tree
#             0
#           /
#          "",2,0
#          /
#         "(",1,1
#         /       \
#        "((",0,2  "()",1,0
#        /            \
#     "(()",0,1       "()(",0,1
#     /                 \
# "(())",0,0            "()()",0,0
# return                  return