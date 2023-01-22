class Solution(object):

    def maximum_wealth(self, accounts):
        bank = []
        for acc in accounts:
            bank.append(sum(acc))

        richest = max(bank)
        return richest
