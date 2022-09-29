from typing import Dict, List
import math


class Statement:

    def __init__(self) -> None:
        self.total_amount = 0
        self.volume_credits = 0
        self.lines: List[str] = []

    def process(self, invoice: Dict, plays: Dict) -> str:
        self._generate_lines(invoice["customer"], invoice["performances"],
                             plays)
        return self._generate_report()

    def _generate_lines(self, customer: str, performances: Dict,
                        plays: Dict) -> None:
        self.lines.append(f'Statement for {customer}')
        for performace in performances:
            play = plays[performace['playID']]

            audience = performace["audience"]
            self.volume_credits += max(audience - 30, 0)

            amount = self._calculate_amount(play, performace)
            self.total_amount += amount

            name = play["name"]
            self._generate_line(name, amount, audience)

    def _calculate_amount(self, play: Dict, performace: Dict) -> int:
        play_type = play["type"]
        audience = performace["audience"]
        if play_type == "tragedy":
            return self._calculate_tragedy_amount(audience)
        if play_type == "comedy":
            return self._calculate_comedy_amount(audience)
        raise ValueError(f'unknown type: {play_type}')

    def _calculate_tragedy_amount(self, audience: int) -> int:
        return int(40000 + 1000 * (audience - 30)) if audience > 30 else 0

    def _calculate_comedy_amount(self, audience: int) -> int:
        self.volume_credits += math.floor(audience / 5)
        amount = 30000 + (300 * audience)
        return amount + 10000 + 500 * (audience -
                                       20) if audience > 20 else amount

    def _generate_line(self, name: str, amount: int, audience: int) -> None:
        amount_in_dollars = self._format_as_dollars(amount)
        self.lines.append(f' {name}: {amount_in_dollars} ({audience} seats)')

    def _generate_report(self) -> str:
        dollars = self._format_as_dollars(self.total_amount)
        return "\n".join([
            *self.lines, f'Amount owed is {dollars}',
            f'You earned {self.volume_credits} credits'
        ])

    @staticmethod
    def _format_as_dollars(amount: float) -> str:
        return f"${amount/100:0,.2f}"
