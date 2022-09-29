from typing import List

from theatrical_players.amount import Amount
from theatrical_players.credit import Credit
from theatrical_players.play import Play


class Report:

    @staticmethod
    def generate(customer: str, plays: List[Play]) -> str:
        credit = Credit()
        amount = Amount()
        lines: List[str] = []

        for play in plays:
            lines.append(play.format())

            credit.add(play.credit)
            credit.add(Credit(max(play.audience - 30, 0)))
            amount.add(play.amount)

        return "\n".join([
            f'Statement for {customer}', *lines,
            f'Amount owed is {amount.format}',
            f'You earned {credit.value} credits'
        ])
