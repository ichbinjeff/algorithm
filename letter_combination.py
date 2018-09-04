class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        rst = []
        level = []
        look_up = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.dfs(rst, level, digits, look_up, 0)
        return rst

    def dfs(self, rst, level, digits, look_up, offset):
        if len(level) == len(digits):
            rst.append("".join(level))
            return

        key = int(digits[offset])
        word = look_up[key]
        for i in range(len(word)):
            level.append(word[i])
            self.dfs(rst, level, digits, look_up, offset+1)
            level.pop()




