from typing import Dict
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
            if play['type'] == "tragedy":
                this_amount = 40000
                if performace['audience'] > 30:
                    this_amount += 1000 * (performace['audience'] - 30)
            elif play['type'] == "comedy":
                this_amount = 30000
                if performace['audience'] > 20:
                    this_amount += 10000 + 500 * (performace['audience'] - 20)

                this_amount += 300 * performace['audience']
            else:
                raise ValueError(f'unknown type: {play["type"]}')

            volume_credits += max(performace['audience'] - 30, 0)
            if "comedy" == play["type"]:
                volume_credits += math.floor(performace['audience'] / 5)
            lines.append(
                f' {play["name"]}: {self._format_as_dollars(this_amount/100)} ({performace["audience"]} seats)'
            )
            total_amount += this_amount

        lines.append(
            f'Amount owed is {self._format_as_dollars(total_amount/100)}')
        lines.append(f'You earned {volume_credits} credits')
        return "\n".join(lines)

    @staticmethod
    def _format_as_dollars(amount: float) -> str:
        return f"${amount:0,.2f}"
