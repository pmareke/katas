from typing import Dict, List
import math


class Statement:

    def __init__(self, invoice: Dict, plays: Dict) -> None:
        self.invoice = invoice
        self.plays = plays
        self.lines: List[str] = [f'Statement for {self.invoice["customer"]}']
        self.total_amount = 0
        self.volume_credits = 0

    def process(self) -> str:
        for performace in self.invoice['performances']:
            play = self.plays[performace['playID']]
            amount = self._play(play, performace)

            self.volume_credits += max(performace['audience'] - 30, 0)
            self.total_amount += amount

            self._statement_line_per_play(play, amount, performace)

        return self._report()

    def _play(self, play: Dict, performace: Dict) -> int:
        if play['type'] == "tragedy":
            this_amount = 40000
            if performace['audience'] > 30:
                this_amount += 1000 * (performace['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000 + (300 * performace['audience'])
            self.volume_credits += math.floor(performace['audience'] / 5)
            if performace['audience'] > 20:
                this_amount += 10000 + 500 * (performace['audience'] - 20)
        else:
            raise ValueError(f'unknown type: {play["type"]}')
        return this_amount

    def _statement_line_per_play(self, play: Dict, amount: int,
                                 performace: Dict) -> None:
        name = play["name"]
        amount_in_dollars = self._format_as_dollars(amount)
        seats = performace["audience"]
        line = f' {name}: {amount_in_dollars} ({seats} seats)'
        self.lines.append(line)

    def _report(self) -> str:
        dollars = self._format_as_dollars(self.total_amount)
        return "\n".join([
            *self.lines, f'Amount owed is {dollars}',
            f'You earned {self.volume_credits} credits'
        ])

    @staticmethod
    def _format_as_dollars(amount: float) -> str:
        return f"${amount/100:0,.2f}"
