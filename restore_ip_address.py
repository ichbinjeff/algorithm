class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rst = []
        self.restore(rst, s, 0)
        return rst

    def restore(self, rst, s, part):
        if part > 3:
            return
        if part == 3 and self.is_valid(s):
            rst.append(s)
            return
        split_by_parts = s.split(".")
        print split_by_parts
        if len(split_by_parts) >= 4:
            return
        for i in range(1, 4):
            if len(split_by_parts) > 1:
                new_pattern = ".".join(split_by_parts[:part])+"."+split_by_parts[part][:i] + "." + split_by_parts[part][i:]
            else:
                new_pattern = split_by_parts[part][:i] + "." + split_by_parts[part][i:]
            self.restore(rst, new_pattern, part+1)

    def is_valid(self, s):
        parts = s.split(".")
        if len(parts) > 4:
            return False
        for i in range(len(parts)):
            if len(parts[i]) > 1 and parts[0] == '0':
                return False
            if int(parts[i]) < 0 or int(parts[i]) > 255:
                return False

        return True



s = Solution()
print s.restoreIpAddresses("25525511135")