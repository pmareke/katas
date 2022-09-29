from typing import Dict, Tuple
import math


class Statement:

    def __init__(self, invoice: Dict, plays: Dict) -> None:
        self.invoice = invoice
        self.plays = plays

    def process(self) -> str:
        total_amount = 0
        volume_credits = 0
        lines = [f'Statement for {self.invoice["customer"]}']
        for performace in self.invoice['performances']:
            play = self.plays[performace['playID']]
            volume_credits, this_amount = self._play(play, performace,
                                                     volume_credits)

            volume_credits += max(performace['audience'] - 30, 0)
            total_amount += this_amount

            lines.append(
                self._statement_line_per_play(play, this_amount, performace))

        lines.append(f'Amount owed is {self._format_as_dollars(total_amount)}')
        lines.append(f'You earned {volume_credits} credits')
        return "\n".join(lines)

    def _play(self, play: Dict, performace: Dict,
              volume_credits: int) -> Tuple[int, int]:
        if play['type'] == "tragedy":
            this_amount = 40000
            if performace['audience'] > 30:
                this_amount += 1000 * (performace['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000 + (300 * performace['audience'])
            volume_credits += math.floor(performace['audience'] / 5)
            if performace['audience'] > 20:
                this_amount += 10000 + 500 * (performace['audience'] - 20)
        else:
            raise ValueError(f'unknown type: {play["type"]}')
        return volume_credits, this_amount

    def _statement_line_per_play(self, play: Dict, amount: int,
                                 performace: Dict) -> str:
        name = play["name"]
        amount_in_dollars = self._format_as_dollars(amount)
        seats = performace["audience"]
        return f' {name}: {amount_in_dollars} ({seats} seats)'

    @staticmethod
    def _format_as_dollars(amount: float) -> str:
        return f"${amount/100:0,.2f}"
