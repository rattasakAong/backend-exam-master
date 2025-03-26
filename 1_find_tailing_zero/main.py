"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        elif number == 0 or number == 1:
            return 0
        else:
            # fac = self.factorial(number)
            fac = self.factorial_with_loop(number)
            count = 0
            for string in reversed(str(fac)):
                if string == '0':
                    count += 1
                else:
                    break
            return count
        
    def factorial(self, n: int) -> int: #max 995
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)
    
    def factorial_with_loop(self, n: int) -> int:
        fac = 1
        for i in range(1, n+1):
            fac *= i
        return fac

#เรียกใช้งาน class
sol = Solution()
test_cases = [7, 10, 100, 200, 0, -10]

for case in test_cases:
    print(f"input = {case}\noutput = {sol.find_tailing_zeroes(case)}")