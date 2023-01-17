class Solution(object):

    def maximumWealth(self, accounts):
        richest = 0
        for acc in accounts:
            bank = 0

            for money in acc:
                bank += money
            if bank > richest:
                richest = bank

        return richest
