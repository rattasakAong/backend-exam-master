"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 10000000:
            return "number can not greater than 10,000,000"
        if number == 0:
            return "ศูนย์"
        
        thai_units = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        thai_numbers = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        
        num_str = str(number)
        length_num_str = len(num_str)
        result = []
        
        # แยกส่วนล้าน (ถ้ามี)
        if length_num_str > 6:
            million_part = num_str[:-6]
            length_million_part = len(million_part)
            remaining_part = num_str[-6:]
            
            # แปลงส่วนล้าน
            for i in range(length_million_part):
                digit = int(million_part[i])
                position = length_million_part - i - 1
                
                if digit == 0:
                    continue
                
                if position == 1 and digit == 1:
                    result.append("สิบ")
                elif position == 1 and digit == 2:
                    result.append("ยี่สิบ")
                elif position == 0 and digit == 1 and length_million_part > 1:
                    result.append("เอ็ด")
                else:
                    result.append(thai_numbers[digit] + thai_units[position])
            
            result.append("ล้าน")
            
            # แปลงส่วนที่เหลือ
            num_str = remaining_part
            length_num_str = len(num_str)
        
        # แปลงส่วนที่เหลือ (น้อยกว่าหรือเท่ากับ 6 หลัก)
        for i in range(length_num_str):
            digit = int(num_str[i])
            position = length_num_str - i - 1
            
            if digit == 0:
                continue
            
            if position == 1 and digit == 1:
                result.append("สิบ")
            elif position == 1 and digit == 2:
                result.append("ยี่สิบ")
            elif position == 0 and digit == 1 and length_num_str > 1:
                result.append("เอ็ด")
            else:
                result.append(thai_numbers[digit] + thai_units[position])
    
        return "".join(result)
        
#เรียกใช้งาน class
sol = Solution()
test_cases = [101, -1, 0, 10, 25, 9999999, 1000000, 10000000, 11000001]

for case in test_cases:
    print(f"input = {case}\noutput = {sol.number_to_thai(case)}")
