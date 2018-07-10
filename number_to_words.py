class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        big_nums = ["Thousand", "Million", "Billion"]
        res = self.convert_less_thousand(num % 1000)
        num //= 1000
        place = 0
        while num > 0:
            converted = self.convert_less_thousand(num % 1000)
            if converted != "":
                res = converted + " " + big_nums[place] if res == "" else converted + " " + big_nums[place] + " " + res
            num //= 1000
            place += 1
        return "Zero" if len(res) == 0 else res

    def convert_less_thousand(self, num):
        less_tw = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                   "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        large_tw = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        hundreds, tens, digits = num // 100, num % 100, num % 10
        res = ""

        if hundreds > 0:
            res = less_tw[hundreds] + " Hundred"
        if tens == 0:
            return res
        if tens < 20:
            if hundreds > 0:
                res += " " + less_tw[tens]
            else:
                res += less_tw[tens]
            return res
        else:
            tens = tens // 10
            res += " " + large_tw[tens] if hundreds > 0 else large_tw[tens]
            res += " " + less_tw[digits] if digits > 0 else ""
        return res

s = Solution()
print s.numberToWords(1000010)