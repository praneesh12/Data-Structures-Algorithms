class Solution:
    def multiply(self, num1, num2):

        if not num1: return num2
        if not num2: return num1
        if not num1 and not num2: return None

        # reverse the digits
        num2 = num2[::-1]
        num1 = num1[::-1]

        ans = 0
        tens_s1 = 1

        for d1 in num1:
            tens_s2 = 1
            for d2  in num2:
                ans += tens_s1*(ord(d1)-ord('0'))*tens_s2*(ord(d2)-ord('0'))
                tens_s2 *= 10
            tens_s1 *= 10
             
        return str(ans)
num1 = "2"
num2 = "124"
s = Solution()
print("num1->",num1, "num2->", num2, "product->", s.multiply(num1, num2))
