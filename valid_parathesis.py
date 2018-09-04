class Solution(object):
    # test case: [[]] {()} {(}} [[ ]]
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {"(":")","{":"}","[":"]"}
        stack = []
        for i in range(len(s)):
            if s[i] in lookup.keys():
                stack.append(s[i])
            elif s[i] in lookup.values():
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if lookup[last] != s[i]:
                    return False
        return len(stack) == 0