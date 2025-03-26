"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if not numbers:
            return "list can not blank"
        
        max_number = numbers[0]
        max_number_index = 0
        
        for i in range(1, len(numbers)):
            if numbers[i] > max_number:
                max_number = numbers[i]
                max_number_index = i

        return max_number_index

#เรียกใช้งาน class
sol = Solution()
test_cases = [[1, 2, 1, 3, 5, 6, 4], [], [10, 20, 30, 5, 2, 30], [9]]

for case in test_cases:
    print(f"input = {case}\noutput = {sol.find_max_index(case)}")