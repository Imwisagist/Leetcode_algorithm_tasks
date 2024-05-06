# https://leetcode.com/problems/design-an-atm-machine/description/
from typing import List


class ATM:

    def __init__(self):
        self.banknotes = [0]*5
        self.nominals = {0: 20, 1: 50, 2: 100, 3: 200, 4: 500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, v in enumerate(banknotesCount): self.banknotes[i] += v * self.nominals[i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0]*5

        for i in range(4, -1, -1):
            res[i] = min(amount // self.nominals[i], self.banknotes[i]); amount -= res[i] * self.nominals[i]

            if not amount:
                for j in range(5): self.banknotes[j] -= res[j]
                return res
            elif amount < 0: break

        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
