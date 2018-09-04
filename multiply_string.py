class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        rst = [0]*(len(num1)+len(num2))
        carry = 0
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                product = num1[i] * num2[j]
                rst[i+j+1] += (carry+product)%10
                rst[i+j] += product/10
                if (rst[i+j]) > 10:
                    carry = rst[i+j]/10
        return "".join(rst).lstrip("0")
