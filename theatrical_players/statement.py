from typing import Dict, List
import math


class Statement:

    def __init__(self) -> None:
        self.total_amount = 0
        self.volume_credits = 0
        self.lines: List[str] = []

    def process(self, invoice: Dict, plays: Dict) -> str:
        customer = invoice["customer"]
        performances = invoice["performances"]
        lines = self._generate_lines(performances, plays)
        return self._generate_report(customer, lines)

    def _generate_lines(self, performances: Dict, plays: Dict) -> List[str]:
        lines: List[str] = []
        for performace in performances:
            play = plays[performace['playID']]

            audience = performace["audience"]
            self.volume_credits += max(audience - 30, 0)

            play_type = play["type"]
            amount = self._calculate_amount(play_type, audience)
            self.total_amount += amount

            name = play["name"]
            lines.append(self._generate_line(name, amount, audience))
        return lines

    def _calculate_amount(self, play_type: str, audience: int) -> int:
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

    def _generate_line(self, name: str, amount: int, audience: int) -> str:
        amount_in_dollars = self._format_as_dollars(amount)
        return f' {name}: {amount_in_dollars} ({audience} seats)'

    def _generate_report(self, customer: str, lines: List[str]) -> str:
        dollars = self._format_as_dollars(self.total_amount)
        lines = [
            f'Statement for {customer}', *lines, f'Amount owed is {dollars}',
            f'You earned {self.volume_credits} credits'
        ]
        return "\n".join(lines)

    @staticmethod
    def _format_as_dollars(amount: float) -> str:
        return f"${amount/100:0,.2f}"
