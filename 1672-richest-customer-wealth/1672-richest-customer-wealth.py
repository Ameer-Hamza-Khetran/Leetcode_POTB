class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        existing_max_wealth = 0
        for i in range(len(accounts)):
            total_money_for_each_customer = 0
            for j in accounts[i]:
                total_money_for_each_customer += j
            if  total_money_for_each_customer > existing_max_wealth:
                existing_max_wealth = total_money_for_each_customer
        return existing_max_wealth