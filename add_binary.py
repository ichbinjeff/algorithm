class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        rst, carry = "", 0
        index_a, index_b = len(a) - 1, len(b) - 1
        while index_a >= 0 or index_b >= 0:
            sum = carry
            if index_a >= 0:
                sum += ord(a[index_a]) - ord('0')
                index_a -= 1

            if index_b >= 0:
                sum += ord(b[index_b]) - ord('0')
                index_b -= 1

            rst = str(sum % 2) + rst
            carry = sum / 2

        if carry > 0:
            rst = str(carry) + rst
        return rst


s = Solution()
s.addBinary("1", "100")
