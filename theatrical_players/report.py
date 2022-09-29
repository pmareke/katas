from dataclasses import dataclass
from typing import List

from theatrical_players.amount import Amount


@dataclass
class Report:
    customer: str
    lines: List[str]

    def generate(self, amount: Amount, volume_credits: int) -> str:
        lines = [
            f'Statement for {self.customer}', *self.lines,
            f'Amount owed is {amount.format}',
            f'You earned {volume_credits} credits'
        ]
        return "\n".join(lines)
