class Solution:
    def roman_to_int(self, s: str) -> int:
        roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}

        roman_list = [char for char in s]
        number = 0
        for index in range(len(roman_list)):
            if index != len(roman_list) - 1:
                if roman_list[index] == 'I' and (roman_list[index + 1] == 'V' or roman_list[index + 1] == 'X'):
                    number -= 2
                elif roman_list[index] == 'X' and (roman_list[index + 1] == 'L' or roman_list[index + 1] == 'C'):
                    number -= 20
                elif roman_list[index] == 'C' and (roman_list[index + 1] == 'D' or roman_list[index + 1] == 'M'):
                    number -= 200

            number += roman[roman_list[index]]
        return number
