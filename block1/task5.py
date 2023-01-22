class Solution:
    def roman_to_int(self, s: str) -> int:
        roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}

        number = 0
        for index in range(len(s)):
            if index != len(s) - 1:
                if s[index] == 'I' and (s[index + 1] == 'V' or s[index + 1] == 'X'):
                    number -= 2
                elif s[index] == 'X' and (s[index + 1] == 'L' or s[index + 1] == 'C'):
                    number -= 20
                elif s[index] == 'C' and (s[index + 1] == 'D' or s[index + 1] == 'M'):
                    number -= 200

            number += roman[s[index]]
        return number
