class Solution(object):

    #3+2*2
    #"14-3/2"
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        number_stack = []
        num = 0
        sign = '+'
        operators = set(['+','-','*','/'])
        s = s.replace(" ", "")
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+int(s[i])
            if s[i] in operators or i == len(s)-1:
                if sign == '+':
                    number_stack.append(num)
                elif sign == '-':
                    number_stack.append(-num)
                elif sign == '*':
                    number_stack.append(number_stack.pop()*num)
                elif sign == '/':
                    b = number_stack.pop()
                    a = b//num
                    if b < 0:
                        a = (b*(-1)/num)*(-1)
                    print "{0}/{1}={2}".format(b, num, a)
                    number_stack.append(a)
                print number_stack
                sign = s[i]
                num = 0

        rst = 0
        for n in number_stack:
            rst += n
        return rst

s = Solution()
print s.calculate("14-3/2")
