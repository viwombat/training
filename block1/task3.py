class Solution(object):

    def maximum_wealth(self, accounts):
        richest = max([sum(acc) for acc in accounts])
        return richest
