class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}

        romanList = [char for char in s]
        sum = 0
        for index in range(len(romanList)):
            if index != len(romanList) - 1:
                if romanList[index] == 'I' and (romanList[index + 1] == 'V' or romanList[index + 1] == 'X'):
                    sum -= 2
                elif romanList[index] == 'X' and (romanList[index + 1] == 'L' or romanList[index + 1] == 'C'):
                    sum -= 20
                elif romanList[index] == 'C' and (romanList[index + 1] == 'D' or romanList[index + 1] == 'M'):
                    sum -= 200

            sum += Roman[romanList[index]]
        return sum